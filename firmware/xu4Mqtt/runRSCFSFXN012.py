import serial
import time
# Define serial port parameters
serial_port = '/dev/ttyUSB0'  # Change this to your serial port
baud_rate = 4800

# Create a serial connection
ser = serial.Serial(serial_port, baud_rate, timeout=.1)

# Define Modbus function code for reading holding registers
function_code = 0x01

# Define the Modbus register address and number of registers to read
register_address    = 0x00
number_of_registers = 2

while True:
    # Build Modbus RTU request frame
    # This is just a basic example; the actual format may vary based on your device
    modbus_request = bytearray([
        0x01,  # Device address
        0x03,  # Function code for reading holding registers
        0x00, 0x00, # Register start address
        0x00, 0x02, # Data Length
        0xC4, 0x0B  # Checksum
    ])

    # Send the Modbus RTU request
    ser.write(modbus_request)

# Read the Modbus RTU response
# response = ser.read(7 + 2 * number_of_registers)  # Adjust the read length based on your expected response size
# print(f"Received data: {response}")

    response = ser.read(7 + 2 * number_of_registers)
    print("---------===============----------")
    print(response)
    print(len(response))
    print("--------------------")
    for x in response:
        print(str(x)+ " - Hex:" +  hex(x)) 
    
    speed          = 256* response[3] +  response[4]
    windDirection  = 256* response[5] +  response[6]

    speed2         = (response[3] << 8) | response[4]
    windDirection2 = (response[5] << 8) | response[6]
    print("---------===============----------")
    print("Speed = " + str(speed/100) + " m/s")
    print("Wind Direction = " + str(windDirection) + " degrees north")
    print("---------===============----------")
    print("Speed = " + str(speed2/100) + " m/s")
    print("Wind Direction = " + str(windDirection2) + " degrees north")    
    print("---------===============----------")
    time.sleep(1)

# Close the serial connection
ser.close()

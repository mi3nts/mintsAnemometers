
import serial
import datetime
from mintsXU4 import mintsSensorReader as mSR
from mintsXU4 import mintsDefinitions as mD
import time
import serial
from collections import OrderedDict

dataFolder    =  mD.dataFolder
rsn012Port    =  mD.rsn012Port[0]
print(rsn012Port)

baudRate = 4800

windSpeedDirectionRequest = bytearray([
                                0x01,  # Device address
                                0x03,  # Function code for reading holding registers
                                0x00, 0x00, # Register start address
                                0x00, 0x02, # Data Length
                                0xC4, 0x0B  # Checksum
                            ])

# windLevelRequest = bytearray([
#                                 0x01,  # Device address
#                                 0x03,  # Function code for reading holding registers
#                                 0x00, 0x04, # Register start address
#                                 0x00, 0x01, # Data Length
#                                 0xC5, 0xCB  # Checksum
#                             ])

def main():

    ser = serial.Serial(
            port = rsn012Port,
            baudrate= baudRate,
            parity  =serial.PARITY_NONE,\
            stopbits=serial.STOPBITS_ONE,\
            bytesize=serial.EIGHTBITS,\
            timeout=0)
    


    while True:
        try:
            print("---------===============----------")
            dateTime  = datetime.datetime.now()
            ser.write(windSpeedDirectionRequest)
            response = ser.read(9)
            print(dateTime)
            print(len(response))
            for x in response:
                print(str(x)+ " - Hex:" +  hex(x)) 
            speed          = (response[3] << 8) | response[4]
            windDirection  = (response[5] << 8) | response[6]
            print("Speed = " + str(speed/100) + " m/s")
            print("Wind Direction = " + str(windDirection) + " degrees north")            
            time.sleep(1)

        except Exception as e:
            # Handle any type of exception
            print(f"An error occurred: {e}")

    ser.close()



if __name__ == "__main__":
    print("=============")
    print("    MINTS    ")
    print("=============")
    if len(rsn012Port)>0:
        print("Monitoring RSN012 Sensor on port: {0}".format(rsn012Port[0])+ " with baudrate " + str(baudRate))
        main()
    else:
        print("Nn RSN012 port found")


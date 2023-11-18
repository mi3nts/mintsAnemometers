
# Code written for RS-CFSFX-N01-2
# Ultrasonic wind speed and
# direction transmitter

import serial
import datetime
from mintsXU4 import mintsSensorReader as mSR
from mintsXU4 import mintsDefinitions as mD
import time
import serial
from collections import OrderedDict

dataFolder    =  mD.dataFolder
rsn012Port    =  str(mD.rsn012Port[0])
baudRate      = 4800
responseTime  = 1
deltaTime     = .000975
sensorName    = "RSN012"

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

def delayTime(startTime,loopTime,deltaTime):
    elapsedTime  = time.time() - startTime
    sleepTime    = max(0,loopTime - elapsedTime-deltaTime)
    time.sleep(sleepTime)
    return time.time();

def main():

    ser = serial.Serial(
            port = rsn012Port,
            baudrate= baudRate,
            parity  =serial.PARITY_NONE,\
            stopbits=serial.STOPBITS_ONE,\
            bytesize=serial.EIGHTBITS,\
            timeout=0.1)
    

    startTime  = time.time()


    while True:
        try:
            dateTime  = datetime.datetime.now()
            ser.write(windSpeedDirectionRequest)
            response = ser.read(9)
            windSpeed          = (response[3] << 8) | response[4]
            windDirection  = (response[5] << 8) | response[6]

            sensorDictionary = OrderedDict([
                    ("dateTime"          ,str(dateTime)),
                    ("windSpeed"         ,windSpeed),
                    ("windDirection"     ,windDirection),
                    ])
            # print(sensorDictionary)
            mSR.sensorFinisher(dateTime,sensorName,sensorDictionary)


            startTime = delayTime(startTime,responseTime,deltaTime)

        except Exception as e:
            # Handle any type of exception
            print(f"An error occurred: {e}")

    ser.close()



if __name__ == "__main__":
    print("=============")
    print("    MINTS    ")
    print("=============")
    if len(rsn012Port)>0:
        print("Monitoring RSN012 Sensor on port: {0}".format(rsn012Port)+ " with baudrate " + str(baudRate))
        time.sleep(1)
        main()
    else:
        print("Nn RSN012 port found")


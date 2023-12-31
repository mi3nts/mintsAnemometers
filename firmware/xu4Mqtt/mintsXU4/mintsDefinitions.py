
from getmac import get_mac_address
import serial.tools.list_ports

# GET RSN012 working 
# get GPS GNGGA Working 
# update node red 


def findPort(find):
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        currentPort = str(p)
        if(currentPort.endswith(find)):
            return(currentPort.split(" ")[0])

def findIPSPorts():
    ports = list(serial.tools.list_ports.comports())
    ipsPorts = []
    for p in ports:
        currentPort = str(p[1])
        if(currentPort.find("CBL-7100")>=0):
            ipsPorts.append(str(p[0]).split(" ")[0])
    return ipsPorts
  
def findAirmarPort():
    ports = list(serial.tools.list_ports.comports())
    ozonePort = []
    for p in ports:
        currentPort = str(p[2])
        if(currentPort.find("PID=10C4:EA60 SER=0001")>=0):
            ozonePort.append(str(p[0]).split(" ")[0])
    return ozonePort

def findRSN012Port():
    ports = list(serial.tools.list_ports.comports())
    ozonePort = []
    for p in ports:
        currentPort = str(p[2])
        if(currentPort.find("USB VID:PID=0403:6001 SER=AU06CSVO")>=0):
            ozonePort.append(str(p[0]).split(" ")[0])
    return ozonePort

def findPortV2(find):
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        currentPort = str(p)
        if(currentPort.find(find)>0):
            return(currentPort.split(" ")[0])
          

def findMacAddress():
    macAddress= get_mac_address(interface="eth0")
    if (macAddress!= None):
        return macAddress.replace(":","")

    macAddress= get_mac_address(interface="docker0")
    if (macAddress!= None):
        return macAddress.replace(":","")

    macAddress= get_mac_address(interface="enp1s0")
    if (macAddress!= None):
        return macAddress.replace(":","")

    macAddress= get_mac_address(interface="wlan0")
    if (macAddress!= None):
        return macAddress.replace(":","")

    return "xxxxxxxx"



dataFolderReference       = "/home/teamlary/mintsData/reference"
dataFolderMQTTReference   = "/home/teamlary/mintsData/referenceMQTT"
dataFolder                = "/home/teamlary/mintsData/raw"
dataFolderMQTT            = "/home/teamlary/mintsData/rawMQTT"


macAddress            = findMacAddress()
latestDisplayOn       = False
latestOn              = False


airmarPort            = findAirmarPort()
rsn012Port            = findRSN012Port()
gpsPort               = findPort("GPS/GNSS Receiver")


# For MQTT 
mqttOn                = True
mqttCredentialsFile   = 'mintsXU4/credentials.yml'
mqttBroker            = "mqtt.circ.utdallas.edu"
mqttPort              =  8883  # Secure port

if __name__ == "__main__":
    # the following code is for debugging
    # to make sure everything is working run python3 mintsDefinitions.py 
    print("Mac Address                : {0}".format(macAddress))
    print("Data Folder Reference      : {0}".format(dataFolderReference))
    print("Data Folder Raw            : {0}".format(dataFolder))
    print("Airmar Port                : {0}".format(airmarPort))
    print("RSN012 Port                : {0}".format(rsn012Port))
    print("GPS Port                   : {0}".format(gpsPort))    
    print("Latest On                  : {0}".format(latestOn))
    print("MQTT On                    : {0}".format(mqttOn))
    print("MQTT Credentials File      : {0}".format(mqttCredentialsFile))
    print("MQTT Broker and Port       : {0}, {1}".format(mqttOn,mqttPort))
    #-------------------------------------------#

# mintsAnemometers
Contains firmware for mints anemometers
  - Airmar
  - RS-CFSFX-N01-2


## Airmar 
The airmar uses RS232 communication protocol. The cables that we typically use would encounter Data out for blue or yellow cables while all others are floating except for power and ground. 

![Airmar](https://raw.githubusercontent.com/mi3nts/mintsAnemometers/main/res/airmarWiring.png)

##  RS-CFSFX-N01-2

The RS-485 standard allows for two different data line configurations:

### RS-485-A:
In the RS-485-A configuration, the A (positive) and B (negative) data lines are connected as follows:
A to A
B to B

### RS-485-B:

In the RS-485-B configuration, the A and B lines are swapped:
A to B
B to A

**The RS-CFSFX-N01-2 follows the RS-485-B convention** 


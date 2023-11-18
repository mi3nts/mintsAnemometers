#!/bin/bash

sleep 60

kill $(pgrep -f 'python3 airMarReader.py')
sleep 1
python3 airMarReader.py &
sleep 5

kill $(pgrep -f 'python3 rsn012Reader.py')
sleep 1
python3 rsn012Reader.py &
sleep 5


kill $(pgrep -f 'python3 gpsReader.py')
sleep 1
python3 gpsReader.py &
sleep 5

python3 ipReader.py


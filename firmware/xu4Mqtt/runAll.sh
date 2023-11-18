#!/bin/bash
#
sleep 60

kill $(pgrep -f 'ips7100ReaderV1.py')
sleep 5
python3 ips7100ReaderV1.py &
sleep 5
kill $(pgrep -f 'python3 rainReader.py')
sleep 5
python3 rainReader.py &
sleep 5
kill $(pgrep -f 'python3 i2cReader.py')
sleep 5
python3 i2cReader.py &
kill $(pgrep -f 'python3 airMarReader.py')
sleep 5
python3 airMarReader.py &
sleep 5
python3 ipReader.py
sleep 5
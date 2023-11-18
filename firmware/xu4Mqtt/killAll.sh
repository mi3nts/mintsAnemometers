#!/bin/bash
#
sleep 1
kill $(pgrep -f 'python3 airMarReader.py')
sleep 1
kill $(pgrep -f 'python3 rsn012Reader.py')
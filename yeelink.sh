#!/bin/sh
python /home/pi/temperature.py

curl --request POST --data-binary @"/home/pi/datafile.txt" --header "xxxx" http://your_url

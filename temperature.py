#!/usr/bin/python
#coding=utf-8
#Filename:temperature.py
import os,datetime,time

def calc_temperature(filename):
    res = 0
    valid_count = 0
    for i in range(0,5):
        with open(filename) as tfile:
            text = tfile.read()
        lines = text.split("\n")
        firstline, secondline = lines[0], lines[1]
        crc = firstline.split(" ")[11]
        if crc == 'YES':
            temperaturedata = secondline.split(" ")[9]
            temperature = float(temperaturedata[2:])
            temperature = temperature / 1000
            valid_count += 1
            res += temperature
        else:
            with open(os.path.expanduser("~/sys.log"), "a") as err:
                err.write("CRC Error: %s\n%s\n" % (datetime.datetime.now().strftime("%Y/%M/%d-%H:%M:%S"), text))
        time.sleep(0.2)
    return res/valid_count if valid_count > 0 else -1

#temperature = calc_temperature("input.txt")
temperature = calc_temperature("/sys/bus/w1/devices/28-000005e31fe6/w1_slave")
if temperature > 0:
    res = '{"value":%f}' %temperature
    with open(os.path.expanduser('~/datafile.txt'), 'w') as output:
        output.write(res)

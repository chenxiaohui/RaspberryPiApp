#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# pir_1.py
# Detect movement using a PIR module
#
# Author : Matt Hawkins
# Date   : 21/01/2013

# Import required Python libraries
import RPi.GPIO as GPIO
import time,os

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_PIR = 4

print "PIR Module Test (CTRL-C to exit)"

# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)      # Echo

Current_State  = 0
Previous_State = 0
last_say_hello_day = 0
valid_hour_range=(20, 23)
dected_motion = True
try:

  print "Waiting for PIR to settle ..."

  # Loop until PIR output is 0
  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0

  print "  Ready"

  # Loop until users quits with CTRL-C
  while True :

    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)

    if Current_State==1 and Previous_State==0:
      # PIR is triggered
      print "  Motion detected!"
      t = time.localtime()
      cur_day = t[2]
      cur_hour = t[3]
      if cur_hour >= valid_hour_range[0] and cur_hour <= valid_hour_range[1]:
          if cur_day != last_say_hello_day:
              #print ("/usr/bin/play -q /home/pi/welcome_back.wav -t alsa")
              os.system ("/usr/bin/play -q /home/pi/welcome_back.wav -t alsa")
              last_say_hello_day = cur_day
          elif dected_motion:
              #print ("/usr/bin/play -q /home/pi/beep.wav -t alsa")
              os.system ("/usr/bin/play -q /home/pi/beep.wav -t alsa")
      # Record previous state
      Previous_State=1
    elif Current_State==0 and Previous_State==1:
      # PIR has returned to ready state
      print "  Ready"
      Previous_State=0

    # Wait for 10 milliseconds
    time.sleep(0.01)

except KeyboardInterrupt:
  print "  Quit"
  # Reset GPIO settings
  GPIO.cleanup()

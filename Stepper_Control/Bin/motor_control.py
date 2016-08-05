#!/usr/bin/python
#Program Title  : countingsteps.py 
#Code Written by: Salty Scott
#Current Project: www.rowboboat.com
#This code is a very basic example of using python to control a spark fun
# easy driver.  The spark fun easy driver that I am using in this example
# is connected to a 42HS4013A4 stepper motor and my raspberry pi.  Pin 23
# is the direction control and pin 24 is the step control.  I am using
# these components in the www.rowboboat.com project version 2.0 and I
# hope someone finds this a useful and simple example.
# This program expects two arguments: direction and steps
# Example usage: sudo python easy_stepper.py left 1600
# The above example would turn a 200 step motor one full revolution as by
# default the easy driver 4.4 is in 1/8 microstep mode.

 

import sys
import signal
import RPi.GPIO as gpio #https://pypi.python.org/pypi/RPi.GPIO more info
import time

 # Functions

def signal_handler(signal, frame):
    print("You interupted me.  How rude!  I was {} steps in!".format(StepCounter))
    # Return running step count
    sys.exit(StepCounter)



# Register function that will handle interupts
signal.signal(signal.SIGINT, signal_handler)


try: 
    direction = sys.argv[1]
    steps = int(float(sys.argv[2]))
    wait_time = float(sys.argv[3])
except:
    direction = 'left' ## new line to set default direction
    steps = 0
 
#print which direction and how many steps 
print("You told me to turn %s %s steps.") % (direction, steps)



# Use for Rasberry Pi's io pins
gpio.setmode(gpio.BCM)




gpio.setup(22, gpio.OUT)    # Motor Controller on/off
gpio.setup(23, gpio.OUT)    # Direction
gpio.setup(24, gpio.OUT)    # Step

 
 
# Set rotation direction
if direction == 'left':
    gpio.output(23, True)
elif direction == 'right':
    gpio.output(23, False)

 
 

# Keep a running total of the numebr of steps taken
StepCounter = 0
 
#waittime controls speed
#WaitTime = 0.01
WaitTime = wait_time

 
 
# Each pulse to the motor controller corresponds to a single motor step.
# We iterate through the required # of steps 
while StepCounter < steps:
 
    #turning the gpio on and off tells the easy driver to take one step
    gpio.output(24, True)
    gpio.output(24, False)
    StepCounter += 1
 
    #Wait before taking the next step...this controls rotation speed
    time.sleep(WaitTime)
#------------------------------------------------------------------------
#------------------------------------------------------------------------
 
 

gpio.cleanup()





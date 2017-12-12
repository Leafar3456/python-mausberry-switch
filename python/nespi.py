#!/usr/bin/env python

# Import the RPi.GPIO and OS
import RPi.GPIO as GPIO
import os
import subprocess

# GPIO port setup
GPIO.setmode(GPIO.BOARD)

# Power switch: will send a shutdown message to the OS
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 16 = 23

# Mausberry circuit: when this pin goes from 1 to 0, the circuit cuts the power to the pi when shut down
GPIO.setup(18, GPIO.OUT) # 18 = 24
GPIO.output(18, 1)

# pause the script and wait for rising pin
GPIO.wait_for_edge(16, GPIO.RISING)

# enable if using killes.sh from 
#https://retropie.org.uk/forum/topic/12895/ensuring-es-gracefully-finish-and-save-metadata-in-every-system-shutdown
#cmd = ['/etc/killes.sh']
#subprocess.Popen(cmd,shell=True).wait()

# Sends a poweroff command to the OS
print('triggering shutdown by hardware')
os.system('poweroff')

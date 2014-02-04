#!/usr/bin/env python2.7  
import RPi.GPIO as GPIO # always needed with RPi.GPIO  
from time import sleep  # pull in the sleep function from time module  
import time
      
GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM  
      
GPIO.setup(8, GPIO.OUT)# set GPIO 25 as output for white led  
#GPIO.PWM(8,5)
#sleep(2)
p = GPIO.PWM(8, 10)    # create object white for PWM on port 25 at 100 Hertz  
p.start(5.0)      
sleep(2)
#p.ChangeDutyCycle(10)
#sleep(2)
#p.stop()

      
GPIO.cleanup()          # clean up GPIO on CTRL+C exit  

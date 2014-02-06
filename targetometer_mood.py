#!/usr/bin/python

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

red = True
green = True
pulse = 0.6
settings = [1,False,False]
while True:
 #read data from file
 f = open('/home/pi/targetometer/data.txt', 'r')
 lines = f.readlines()
 f.close()
 settings = lines[0].split(";")
 if settings[0]:
  pulse = float(settings[0])
 if settings[1]:
  red = settings[1]
 if settings[2]:
  green = settings[2]

 #print(settings)
 blink = 0
 while blink < 20:
  GPIO.output(11, False)
  GPIO.output(13, False)
  sleep(pulse)
  if green == "on":
   GPIO.output(11, True)
  if red == "on":
   GPIO.output(13, True)
  sleep(pulse)
  blink = blink + 1

GPIO.cleanup()

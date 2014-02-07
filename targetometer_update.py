#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
import RPi.GPIO as GPIO
import os
import sys

lcd = Adafruit_CharLCDPlate()
lcd.backlight(lcd.ON)

#check if i am already running
#f = open('/home/pi/targetometer/lock.txt', 'r')
#lockstate = f.read()
#f.close()
#print "Lockstate:" + lockstate
#if lockstate == "1":
# sys.exit()
#else:
# f2 = open('/home/pi/targetometer/lock.txt', 'w')
# f2.write("1")
#f2.close()


#print lockstate

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

GPIO.output(16, False)
GPIO.output(18, False)
GPIO.output(22, False)
GPIO.output(24, False)
GPIO.output(26, False)
sleep(1)

#turn them on
GPIO.output(18, True)
sleep(0.05)
GPIO.output(18, False)
sleep(0.08)
GPIO.output(18, True)
sleep(1.5)
GPIO.output(26, True)
sleep(0.5)
GPIO.output(22, True)
sleep(0.7)
GPIO.output(24, True)
sleep(0.3)

blink = 0
while (blink < 10):
 GPIO.output(16, True)
 sleep(0.06)
 GPIO.output(16, False)
 sleep(0.06)
 blink = blink +1

# Clear display and show some status messages
loop=0;
while (loop < 2):
 lcd.backlight(lcd.RED)
 lcd.clear()
 lcd.message("nugg.ad \ntargetometer")
 sleep(3)
 lcd.clear()

 #check internet and IP adress
 import socket
 ip = ""
 try:
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(('nugg.ad', 0))
  ip = s.getsockname()[0]
  if ip != "":
   lcd.message("IP-Adresse:\n" + ip)
   sleep(2)
  else:
   lcd.message("connection error")
  sleep(2)
  lcd.clear()
 except:
  pass

 lcd.message("Predictions:\n23785 (+3%)")
 sleep(3)
 lcd.clear()
 lcd.message("Programmatic:\n12300 (+11%)")
 sleep(3)
 lcd.clear()
 lcd.message("Campaigns:\n23")
 sleep(3)
 lcd.clear()
 lcd.message("best var:\nSUV")
 sleep(3)
 lcd.clear()
 lcd.message("brand uplift:\n+23%")
 sleep(3)
 lcd.clear()
 lcd.message("Enjoy your\n weekend")
 sleep(3)
 lcd.clear()
 sleep(0.2)
 lcd.message("you little\n sucker")
 sleep(0.7)
 lcd.clear()
 loop = loop + 1

f = open('/home/pi/targetometer/lock.txt', 'w')
f.write("0")
f.close()

lcd.backlight(lcd.OFF)

GPIO.cleanup()

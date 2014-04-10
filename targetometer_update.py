#!/usr/bin/python

from time import sleep, strftime, localtime
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
import RPi.GPIO as GPIO
import os
import sys
from jsonreader2 import flat

lcd = Adafruit_CharLCDPlate()
lcd.backlight(lcd.ON)


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

while(1==1):
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
 #loop=0;
 lcd.backlight(lcd.RED)
 lcd.clear()
 lcd.message("nugg.ad \ntargetometer")
 sleep(3)
 lcd.clear()
 lcd.message(strftime("%a, %d %b %Y \n %H:%M:%S", localtime()))
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

#display some kpis from the list
 for index  in flat:
  lcd.message(index[0] + "\n" + str(index[1]))
  sleep(3)
  lcd.clear()

 lcd.message("Enjoy your\n weekend")
 sleep(3)
 lcd.clear()
 sleep(0.2)
 lcd.message("my\n friend")
 sleep(0.7)
 lcd.clear()
 #loop = loop + 1
 
 GPIO.output(16, False)
 GPIO.output(18, False)
 GPIO.output(22, False)
 GPIO.output(24, False)
 GPIO.output(26, False)

 t = 0
 while(t < 60):
  lcd.message(strftime("%a, %d %b %Y \n %H:%M:%S        ", localtime()))
  sleep(1)
  t = t+1

lcd.backlight(lcd.OFF)

GPIO.cleanup()

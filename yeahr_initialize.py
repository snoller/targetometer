#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
import RPi.GPIO as GPIO
import os

lcd = Adafruit_CharLCDPlate()
lcd.clear()
lcd.message("nugg.ad\n Yeah Receiver")
sleep(1)
lcd.clear()
lcd.message("initializing...")
sleep(2)
lcd.clear()

#check internet and IP adress
import socket
ip = ""
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('google.com', 0))
ip = s.getsockname()[0]
if ip != "":
 lcd.message("IP-Adresse:\n" + ip)
else:
 lcd.message("connection error")
sleep(2)
lcd.clear()

#LEDs checken
lcd.message("checking ...")
sleep(2)
#lcd.clear()
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)

GPIO.output(7, False)
sleep(2)

#turn them on
GPIO.output(7, True)
sleep(1)
lcd.clear()
sleep(0.5)

lcd.backlight(lcd.OFF)
lcd.clear()


GPIO.cleanup()

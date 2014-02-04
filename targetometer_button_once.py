#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
import os

lcd = Adafruit_CharLCDPlate()

GPIO.setmode(GPIO.BCM)

GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)


GPIO.output(4, False)
GPIO.output(8, False)
GPIO.output(9, False)
GPIO.output(10, False)
GPIO.output(11, False)
sleep(1)
GPIO.output(11, True)

lcd.clear()
lcd.message("Updating.")
sleep(1)
lcd.clear()
lcd.message("Updating..")
sleep(1)
lcd.clear()
lcd.message("Updating...")
sleep(1.8)
lcd.clear()
lcd.message("Updating....")
sleep(1.8)
lcd.clear()
lcd.message("Updating.....")
sleep(1.8)
lcd.clear()
lcd.message("Ready")
sleep(1)
lcd.clear()
#lcd.message("nugg.ad \ntargetometer")
os.system("python /home/pi/targetometer/targetometer_update.py")

GPIO.cleanup()

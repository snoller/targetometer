#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
import os

lcd = Adafruit_CharLCDPlate()

GPIO.setmode(GPIO.BOARD)

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
GPIO.output(18, True)

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

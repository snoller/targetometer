#!/usr/bin/python

from time import sleep, strftime, localtime
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
import RPi.GPIO as GPIO
import os
import sys

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

lcd = Adafruit_CharLCDPlate()
lcd.backlight(lcd.RED)
i = 0

while(i<20):
 lcd.message("nugg.ad \nYeah Receiver")
 sleep(10)
 lcd.clear()
 lcd.message("Received Yeah\nfrom ASMI")

 GPIO.setup(7, GPIO.OUT)
 GPIO.output(7, False)
 sleep(5)
 GPIO.output(7, True)
 lcd.clear()
 #lcd.message("Waiting for Yeahs \nsince 23 minutes")
 #sleep(10)
 #lcd.clear()
 i = i+1
lcd.backlight(lcd.OFF)
lcd.clear()
 
GPIO.cleanup()

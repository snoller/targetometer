#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
import RPi.GPIO as GPIO
import os

lcd = Adafruit_CharLCDPlate()
lcd.clear()
lcd.message("nugg.ad\n targetometer")
sleep(1)
lcd.clear()
lcd.message("initializing...")
sleep(2)
lcd.clear()

#check internet and IP adress
import socket
ip = ""
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('nugg.ad', 0))
ip = s.getsockname()[0]
if ip != "":
 lcd.message("IP-Adresse:\n" + ip)
else:
 lcd.message("connection error")
sleep(2)
lcd.clear()

#LEDs checken
lcd.message("checking LEDs...")
sleep(2)
#lcd.clear()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
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

#turn them on
GPIO.output(11, True)
sleep(0.5)
GPIO.output(11, False)
sleep(0.5)
GPIO.output(9, True)
sleep(0.5)
GPIO.output(9, False)
sleep(0.5)
GPIO.output(8, True)
sleep(0.5)
GPIO.output(8, False)
sleep(0.5)
GPIO.output(10, True)
sleep(0.5)
GPIO.output(10, False)
sleep(0.5)
GPIO.output(4, True)
sleep(0.5)
GPIO.output(4, False)
lcd.clear()
sleep(0.5)

lcd.message("fetching data...")
sleep(3)
os.system("python /home/pi/targetometer/targetometer_button_once.py")

GPIO.cleanup()

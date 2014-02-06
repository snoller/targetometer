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
s.connect(('google.com', 0))
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
sleep(0.5)
GPIO.output(18, False)
sleep(0.5)
GPIO.output(18, True)
sleep(0.5)
GPIO.output(18, False)
sleep(0.5)
GPIO.output(16, True)
sleep(0.5)
GPIO.output(16, False)
sleep(0.5)
GPIO.output(22, True)
sleep(0.5)
GPIO.output(22, False)
sleep(0.5)
GPIO.output(24, True)
sleep(0.5)
GPIO.output(24, False)
sleep(0.5)
GPIO.output(26, True)
sleep(0.5)
GPIO.output(26, False)
sleep(1)
lcd.clear()
sleep(0.5)

lcd.message("fetching data...")
sleep(3)
os.system("python /home/pi/targetometer/targetometer_button_once.py")

GPIO.cleanup()

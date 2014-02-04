import RPi.GPIO as GPIO
from time import sleep
import time
import os
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
lcd = Adafruit_CharLCDPlate()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

switch = 0
lastpushed = 0
while True:
	if GPIO.input(25):
		if (time.time() - lastpushed < 0.3):	
			switch = 2
			print "double"
		elif (time.time() - lastpushed > 2):
			switch = 1
			print "single"
		lastpushed = time.time()
	#print "lastpushed: " + str(lastpushed) + " time: " + str(time.time())	
	#print "\ntimediff: " + str(time.time() - lastpushed)
	if switch==1:
		os.system("python /home/pi/targetometer/targetometer_button_once.py")
		switch = 0
	if switch==2:
		lcd.clear()
		lcd.message("ok we'll contact\nyou asap")
		sleep(1)
		lcd.clear()
		switch = 0
	sleep(0.1)

GPIO.cleanup()


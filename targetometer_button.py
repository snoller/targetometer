import RPi.GPIO as GPIO
from time import sleep
import time
import os
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
lcd = Adafruit_CharLCDPlate()

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
 while True:
  GPIO.wait_for_edge(15, GPIO.FALLING)
  os.system("python /home/pi/targetometer/targetometer_button_once.py")

except KeyboardInterrupt:
 GPIO.cleanup()

GPIO.cleanup()

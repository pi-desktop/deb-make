#!/user/bin/env python

import RPi.GPIO as GPIO
import time
import os,sys
import signal

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.IN)

GPIO.output(31,GPIO.LOW)
 
def shutdown_system(channels):
    os.system("sync")
    time.sleep(1)
    os.system("shutdown -h now")
    sys.exit()


GPIO.add_event_detect(33,GPIO.RISING,callback=shutdown_system)

while True:
    time.sleep(1)

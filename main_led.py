#/user/bin/env python

import RPi.GPIO as GPIO
import entitis
from sakshat import SAKSHAT
import time

SAKS = SAKSHAT()

def water_light():
    for i in range(0,8):
        SAKS.ledrow.on_for_index(i)
        time.sleep(0.1)
	SAKS.ledrow.off_for_index(i)
	time.sleep(0.1)

if __name__ == "__main__":
    try:
        while True:
            water_light()
    except KeyboardInterrupt:
        print "end water light..."
        SAKS.ledrow.off()
        GPIO.cleanup()

  #!/user/bin/env python

import RPi.GPIO as GPIO
from sakspins import SAKSPins as pins
import entitis

class SAKSHAT(object):
    ledrow = None
    digital_display = None
    def sak_gpio_init(self):
        GPIO.setwarnings(False)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)

        for i in [pins.IC_74HC595_DS,pins.IC_74HC595_SHCP,pins.IC_74HC595_STCP,pins.IC_TM1637_DI,pins.IC_TM1637_CLK]:
            GPIO.setup(i,GPIO.OUT)
            GPIO.output(i,GPIO.LOW)

    def __init__(self):
        self.sak_gpio_init()
        self.ledrow = entitis.Led74HC595({'ds':pins.IC_74HC595_DS, 'shcp':pins.IC_74HC595_SHCP, 'stcp':pins.IC_74HC595_STCP},GPIO.HIGH)
        self.digital_display = entitis.DesplayByIC_TM1673({'di':pins.IC_TM1637_DI , 'clk':pins.IC_TM1637_CLK},GPIO.HIGH)

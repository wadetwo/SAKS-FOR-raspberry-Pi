#/user/bin/env python

import RPi.GPIO as GPIO
from .ic_74ch import IC_74HC595 as ic74hc

class Led74HC595(object):
    '''
    claass of leds in 74hc595
    '''
    __ic_74hc595 = None
    def __init__(self,pins,real_true = GPIO.HIGH):
        '''
        init the leds
        '''
        self.__ic_74hc595 = ic74hc(pins,real_true)

    #status.
    def ic(self):
        return self.__ic_74hc595

    def is_on(self,index):
        '''
        get the status of led in ledrow by index
        '''
        if index >= 8:
            return False
        return self.__ic_74hc595.data() >> index & 0x01
    def row_status(self):
        r = []
        for i in range(0,8):
            r.append(self.__ic_74hc595.data >> index & 0x01)
        return r

    def on(self):
        '''
        set all leds on
        '''
        self.__ic_74hc595.set_data(0xff)

    def off(self):
        self.__ic_74hc595.clear()

    def on_for_index(self, index):
        #self.__ic_74hc595.set_data(self.__ic_74hc595.data | (0x01 << (index)))
        self.__ic_74hc595.set_data(self.__ic_74hc595.data() | (0x01 << (index)))


    def off_for_index(self, index):
        off = [0xfe,0xfd,0xfb,0xf7,0xef,0xdf,0xbf,0x7f]
        self.__ic_74hc595.set_data(self.__ic_74hc595.data() & off[index])

    def set_row(self,status):
        '''
        set the ledrow's status in boolean array
        '''
        for i in range(len(status)):

            if status[i] is None:
                continue
            if status[i]:
                self.on_for_index(i)
            else :
                self.off_for_index(i)

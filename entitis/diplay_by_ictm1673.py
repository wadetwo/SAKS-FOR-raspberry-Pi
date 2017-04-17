#/user/bin/env python

import RPi.GPIO as GPIO
import re
from .ic_tm1673 import IC_TM1673 as tm1673

class DesplayByIC_TM1673(object):
    __is_on = False
    __numbers = []
    __ic_tm1673 = None
    __number_code = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f, 0x00, 0x40]
    __address_code = [0xc0, 0xc1, 0xc2, 0xc3]
    def __init__(self,pins,real_true = GPIO.HIGH):

        self.__ic_tm1673 = tm1673(pins,real_true)

    def is_on(self):
        return self.__is_on

    def numbers(self):
        return self.__numbers

    def set_numbers(self,value):
        pattern = re.compile(r'[-|#|\d]\.?')
        matchs = pattern.findall(value)

        self.__numbers = []
        for i in range(len(matchs)):
            self.__numbers.append(matchs[i])

    def IC(self):
        return self.__ic_tm1673

    def set_on(self):
        self.__ic_tm1673.set_command(0x8f)
        __is_on = True

    def set_off(self):
        self.__ic_tm1673.clear()
        __is_on = False

    
    def show(self, str):
        '''
        Set the numbers array to show and enable the display
        :return: void
        '''
        self.set_numbers(str)
        #print(self.__numbers)

        self.__ic_tm1673.set_command(0x44)

        for i in range(min(4, len(self.__numbers))):
            dp = True if self.__numbers[i].count('.') > 0 else False
            num = self.__numbers[i].replace('.','')
            if num == '#':
                num = 10
            elif num == '-':
                num = 11
            else:
                num = int(num)

            if dp:
                self.__ic_tm1673.set_data(self.__address_code[i], self.__number_code[num]|0x80)
            else:
                self.__ic_tm1673.set_data(self.__address_code[i], self.__number_code[num])

        self.set_on()

        

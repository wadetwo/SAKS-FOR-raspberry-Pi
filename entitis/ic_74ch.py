#!/user/bin/env python

import RPi.GPIO as GPIO

class IC_74HC595(object):
    '''
    IC_74HC595 class
    '''
    __pins = {'ds':0, 'shcp':0, 'stcp':0}
    __real_true = GPIO.HIGH
    __data = 0x00

    def __init__(self,pins,real_true = GPIO.HIGH):
        self.__pins = pins;
        self.__real_true = real_true

    def data(self):
        '''
        return the data
        :return: void
        '''
        return self.__data

    def flush_shcp(self):
        '''
        flush the  shcp
        '''
        GPIO.output(self.__pins['shcp'],not self.__real_true)
        GPIO.output(self.__pins['shcp'],self.__real_true)

    def flush_stcp(self):
        '''
        flush a stcp
        '''
        GPIO.output(self.__pins['stcp'],not self.__real_true)
        GPIO.output(self.__pins['stcp'],self.__real_true)
    def set_bit(self,bit):
        GPIO.output(self.__pins['ds'],bit)
        self.flush_shcp()

    def set_data(self,data):

        self.__data = data
        for i in range(0,8):
            self.set_bit((self.__data>>i)&0x01)
        self.flush_stcp()

    def clear(self):
        self.set_data(0x00);
        
    
    

#/user/bin/env python

import RPi.GPIO as GPIO
import time

class IC_TM1673(object):
    __pins = {'di':0 , 'clk':0}
    __real_true = GPIO.HIGH

    def __init__(self,pins,real_true=GPIO.HIGH):
        '''
        init the pins
        '''
        self.__pins = pins
        self.__real_true = real_true

    def bus_delay(self):
        time.sleep(0.001)

    
    def start_bus(self):
        GPIO.output(self.__pins['clk'], self.__real_true)
        GPIO.output(self.__pins['di'], self.__real_true)
        self.bus_delay()
        GPIO.output(self.__pins['di'],not self.__real_true)
        self.bus_delay()
        GPIO.output(self.__pins['clk'],not self.__real_true)
        self.bus_delay()


    def stop_bus(self):
        GPIO.output(self.__pins['clk'], not self.__real_true)
        self.bus_delay()
        GPIO.output(self.__pins['di'], not self.__real_true)
        self.bus_delay()
        GPIO.output(self.__pins['clk'], self.__real_true)
        self.bus_delay()
        GPIO.output(self.__pins['di'], self.__real_true)
        self.bus_delay()

    def set_bit(self, bit):
        '''
        start abit
        '''
        GPIO.output(self.__pins['clk'],not self.__real_true)
        self.bus_delay()
        GPIO.output(self.__pins['di'],bit)
        self.bus_delay() 
        GPIO.output(self.__pins['clk'],self.__real_true)
        self.bus_delay()

    def set_byte(self,data):
         for i in range (0,8):
             self.set_bit((data >> i) & 0x01)

         GPIO.output(self.__pins['clk'], not self.__real_true)
         self.bus_delay()

         GPIO.output(self.__pins['di'], self.__real_true)
         self.bus_delay()

         GPIO.output(self.__pins['clk'], self.__real_true)
         self.bus_delay()

    def set_command(self,command):
        self.start_bus()
        self.set_byte(command)
        self.start_bus()
    def set_data(self, address, data):
        '''
        Set data with address and data
        :param address: address
        :param data: data
        :return: void
        '''
        self.start_bus()
        self.set_byte(address)
        self.set_byte(data)
        self.start_bus()

    def clear(self):
        '''
        Clear the data
        :return: void
        '''
        self.set_command(0x80) 
    

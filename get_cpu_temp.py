#/user/bin/env python

import entitis
import commands
from sakshat import SAKSHAT

SAKS = SAKSHAT()
def get_cpu_temperature():
    cpu_temp = open('/sys/class/thermal/thermal_zone0/temp','r')
    temperature = cpu_temp.read()
    cpu_temp.close()
    return float(temperature) / 1000

def get_gpu_temperature():
    gpu_temp = commands.getoutput('/opt/vc/bin/vcgencmd measure_temp').replace('temp=','').replace('\'C','')
    return float(gpu_temp)

if __name__ == "__main__":
    temp = get_cpu_temperature()
    SAKS.digital_display.show("%2f" % temp)
    input("put any key to end...")
    

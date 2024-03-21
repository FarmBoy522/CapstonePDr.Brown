from machine import Pin, ADC
from debounced_input import DebouncedInput
import time
import rp2

def setandinit():
    #LED Pins Control 
    p0 = Pin(2, mode=Pin.OUT, pull=None, value=1)
    p1 = Pin(3, mode=Pin.OUT, pull=None, value=1)
    p2 = Pin(4, mode=Pin.OUT, pull=None, value=1)
    p3 = Pin(5, mode=Pin.OUT, pull=None, value=1)
    p4 = Pin(6, mode=Pin.OUT, pull=None, value=1)
    p5 = Pin(7, mode=Pin.OUT, pull=None, value=1)
    p6 = Pin(8, mode=Pin.OUT, pull=None, value=1)
    p7 = Pin(9, mode=Pin.OUT, pull=None, value=1)
    p8 = Pin(10, mode=Pin.OUT, pull=None, value=1)
    p9 = Pin(11, mode=Pin.OUT, pull=None, value=1)
    p10 = Pin(12, mode=Pin.OUT, pull=None, value=1)
    p11 = Pin(13, mode=Pin.OUT, pull=None, value=1)
    
    #ADC Input Pins
    voltage1 = ADC(Pin(26))
    voltage2 = ADC(Pin(27))
    
    #Pulse Control Pins
    ctrl1 = Pin(14, mode=Pin.OUT, pull=None, value=0)
    ctrl2 = Pin(15, mode=Pin.OUT, pull=None, value=0)
    
    #Input Control Pins
#     strt = DebouncedInput(20, callback, pin_pull=Pin.PULL_DOWN)
#     stop = DebouncedInput(19, callback, pin_pull=Pin.PULL_DOWN)
#     slct = DebouncedInput(18, callback, pin_pull=Pin.PULL_DOWN)
    
    strt = Pin(20, mode=Pin.IN, pull=Pin.PULL_DOWN)
    stop = Pin(19, mode=Pin.IN, pull=Pin.PULL_DOWN)
    slct = Pin(18, mode=Pin.IN, pull=Pin.PULL_DOWN)
    
    
    #Array of Pin Objects
    #Array Num	0	1	2	3	4	5	6	7	8	9	10	 11		12		 13			14	   15	 16    17	 18
    PinArray = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, voltage1, voltage2, ctrl1, ctrl2, strt, stop, slct]
    #Pin Val	2	3	4	5	6	7	8	9	10	11	12	 13		26		 27			14	   15	 20	   19	 18
    
    return PinArray

def callback(pin, pressed, duration_ms):
    if (pressed):
        print("Pin-", pin, " Pressed:", duration_ms, "ms since last press")
        return 1
    else:
        print("Pin-", pin, " Released:", duration_ms, "ms long press")
        return 0
        
def debounce(pin):
    # wait for pin to change value
    # it needs to be stable for a continuous 20ms
    cur_value = pin.value()
    active = 0
    while active < 20:
        if pin.value() != cur_value:
            active += 1
        else:
            active = 0
        time.sleep_ms(1)
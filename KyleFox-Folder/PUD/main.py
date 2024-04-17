# Main file, runs whole program
# Currently used in one file to simplify cross file variables
# Plan to change in future update
# V1.0 - Full Working Version #1

import time
from machine import Pin, ADC
from debounced_input import DebouncedInput
import rp2
import setup
import programs

# PIO 50 Pulse Generator
@rp2.asm_pio(set_init=rp2.PIO.OUT_HIGH)
def pulse_management():
    # Total Loop Label
    label("total_pulse")
    
    # Cycles: 1 + 6 + 32 * (2 + 1) = 117 cycles
    # 1 set, 5 set + delay, 32 label + nop + jmp, repeat 3 times
    set(pins, 0)
    set(x, 2)                   [5]
    label("delay_high")
    nop()                       [29]
    jmp(x_dec, "delay_high")

    # Cycles: 1 + 1 + 6 + 157 * (30 + 1) = 5115 cycles
    # 1 nop, 1 set, 5 set + delay, 157 label + nop + jmp, repeat 31 times
    nop()
    set(pins, 1)
    set(x, 30)                  [5]
    label("delay_low")
    nop()                       [29]
    nop()                       [29]
    nop()                       [29]
    nop()                       [29]
    nop()                       [29]
    nop()                       [9]
    jmp(x_dec, "delay_low")
    jmp(y_dec, "total_pulse")
    
    # End by looping indefinitely
    label("noperation")
    nop()
    jmp("noperation")

def ControlStateMachine(PinArray):
    flag = 1
    global state
    
    #Input Control Pins
    strt = DebouncedInput(20, startcall, pin_pull=Pin.PULL_DOWN)
    stop = DebouncedInput(19, stopcall, pin_pull=Pin.PULL_DOWN)
    slct = DebouncedInput(18, selectcall, pin_pull=Pin.PULL_DOWN)
    
    while flag == 1:
        # STATE 0 - WAIT FOR BUTTON PRESS - This is the stop state
        if state == 0:
            print(state)
            time.sleep(2)
                    
        # STATE 1 - RUN PROGRAM
        elif state == 1:
            print(state)
            #programs.state1(timeset, piosm, PinArray)
            state = 0
            
        # STATE 2 - CHANGE TOTAL TEST TIME
        elif state == 2:
            print(state)
            #sec, currentset = programs.state2(currentset, flag)
            state = 0
            
        # ERROR STATE - SOMETHING HAS GONE WRONG AND EXIT
        else:
            print(state)
            print("Error: Wrong State")
            flag = 0
            exit
            
            
    print("Crashed - Check for Errors")
    
def startcall(pressed):
    global state
    if pressed == True:
        state = 1
        
def stopcall(pressed):
    global state
    if pressed:
        state = 0
        

def selectcall(pressed):
    global state
    if pressed:
        state = 2


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
    
    #Array of Pin Objects
    #Array Num	0	1	2	3	4	5	6	7	8	9	10	 11		12		 13
    PinArray = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, voltage1, voltage2]
    #Pin Val	2	3	4	5	6	7	8	9	10	11	12	 13		26		 27
    
    return PinArray

def state1(timeset, piosm, PinArray):
    # Create the StateMachine with the pulse_management program, outputting on Pin(14).
    sm = rp2.StateMachine(0, pulse_management, freq=500000, set_base=Pin(14))

    # Load the total pulse value into the TX FIFO then load into Y register.
    sm.put(49)					# Total pulses of 50
    sm.exec("pull()")			# Pull from TX FIFO to OSR
    sm.exec("mov(y,osr)")		# Move from OSR to Y
    
    # Device starts charging
    time.sleep(600) # Wait 10min before checking ADC
    
    # Check the ADC voltage
    if voltage1.read_u16() > 100:   # If voltage is good 
        smpulse.active(1)
        time.sleep_ms(100)
    else:
        time.sleep(60)
        fail += 1
    smpulse.active(0)
    #decriment time from total test time
    print("imagine code here")
    
def state2(currentset):
    
    # If the debug mode is set, run for 10min only
    if currentset == -1:
        print("Debug Mode")
        testcounter = 1
        currentset = -1
        return testcounter, currentset
    else:
        # If debug mode isnt selected operate as normal
        testcounter = [1, 36, 72, 144, 288, 432]		# Hour selections; 6hr / 10min = 36 instances
        currentset += 1							# Incriment the current hour select to next one
        
        return testcounter, currentset

if __name__ == '__main__':
    global state
    state = 0

    # Start the StateMachine.
    #sm.active(1)    
    
    PinArray = setandinit()
    ControlStateMachine(PinArray)

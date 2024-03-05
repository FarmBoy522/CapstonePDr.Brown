import time
from machine import Pin
import rp2
import setup
import programs

def ControlStateMachine(PinArray):
    state = 0
    flag = 1
    
    while flag == 1:
        # STATE 0 - WAIT FOR BUTTON PRESS
        if state == 0:
            while state == 0:
                if setup.debounce(PinArray[16]) == 1:		#Start Button Pushed
                    print("Button pushed")
                    state = 1
                elif PinArray[17] == 1:		#Stop Button Pushed
                    state = 0
                elif PinArray[18] == 1:		#Select Button Pushed
                    state = 2
        # STATE 1 - RUN PROGRAM
        elif state == 1:
            programs.state1(timeset, piosm, PinArray)
        # STATE 2 - CHANGE TOTAL TEST TIME
        elif state == 2:
            sec, currentset = programs.state2(currentset, flag)
        # ERROR STATE - SOMETHING HAS GONE WRONG AND EXIT
        else:
            print("Error: Wrong State")
            flag == 0
            exit
    print("Crashed - Check for Errors")

if __name__ == '__main__':
    PinArray = setup.setandinit()
    ControlStateMachine(PinArray)
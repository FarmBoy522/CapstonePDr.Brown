from debounced_input import DebouncedInput
import machine
import micropython
import time

micropython.alloc_emergency_exception_buf(100)

# Define button press/release callback
def callback(pin, pressed, duration_ms):
    if (pressed):
        print("Pin-", machine.pin, " Pressed:", duration_ms, "ms since last press")
    else:
        print("Pin-", machine.pin, " Released:", duration_ms, "ms long press")
        
def callback2(pressed):
    global state
    if (pressed):
        state = 1
        
def callback3(pressed):
    global state
    if (pressed):
        state = 2
    
button1 = DebouncedInput(20, callback2, pin_pull=machine.Pin.PULL_DOWN)
button2 = DebouncedInput(19, callback3, pin_pull=machine.Pin.PULL_DOWN)

global state
state = 0

while True:
    global state
    
    if state == 1:
        print("state 1")
        state = 0
    elif state == 2:
        print("state 2")
        state = 0
    else:
        print("nothing")
        
    time.sleep(3.5)
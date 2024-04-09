"""
From JMCCLIN2 on github
https://github.com/jmcclin2/updebouncein
Modified by Kyle Fox
    Changed Callback function to only send false and true boolean
"""
from machine import Pin, Timer
import time


class DebouncedInput:
    """Micropython Debounced GPIO Input Class"""
    # Initializes the class child with pin number, callback function, pin_pull direction, pin_logic direction, and debounce wait time.
    def __init__(self, pin_num, callback, pin_pull=None, pin_logic_pressed=True, debounce_ms=100):
        self.pin_num = pin_num
        self.pin_pull = pin_pull
        self.pin_logic_pressed = pin_logic_pressed
        self.debounce_ms = debounce_ms
        self.callback = callback
        self.last_release_ms = 0
        self.last_press_ms = 0

        self.pin = Pin(self.pin_num, Pin.IN, self.pin_pull)
        self.pin.irq(self.__ButtonHandler, Pin.IRQ_FALLING | Pin.IRQ_RISING)
    
        self.db_timer = Timer(-1)
        self.expected_value = True

    # Check timer 
    def __ButtonDebounceTimerExpired(self, timer):
           
        current_value = False   
           
        if (self.pin.value() == self.pin_logic_pressed):
            current_value = True
        else:
            current_value = False
        
        if ((self.expected_value == True) and (current_value == True)):
            self.expected_value = False
            self.last_press_ms = time.ticks_ms()
            
            if (self.last_release_ms == 0):
                ms_since_last_press = 0
            else:
                ms_since_last_press = time.ticks_diff(self.last_press_ms, self.last_release_ms) + 2*self.debounce_ms
                
            #self.callback(self.pin_num, True, ms_since_last_press)
            self.callback(True)
            
        elif ((self.expected_value == False) and (current_value == False)):
            self.expected_value = True
            self.last_release_ms = time.ticks_ms()
            ms_duration_of_press = time.ticks_diff(self.last_release_ms, self.last_press_ms) + 2*self.debounce_ms
            #self.callback(self.pin_num, False, ms_duration_of_press)
            self.callback(False)
            
        # Re-enable pin interrupt
        self.pin.irq(self.__ButtonHandler, Pin.IRQ_FALLING | Pin.IRQ_RISING)

    # Set timer and disable pin interrupt
    def __ButtonHandler(self, pin):
        
        # Set timer
        self.db_timer.init(mode=Timer.ONE_SHOT, period=self.debounce_ms, callback=self.__ButtonDebounceTimerExpired)
        
        # Disable pin interrupt
        self.pin.irq(trigger=0)
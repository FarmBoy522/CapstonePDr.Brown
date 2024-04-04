# Main file, runs whole program

import time
from machine import Pin
import rp2


# PIO 50 Pulse Generator
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def pulse_management():
    # 
    label("total_pulse")
    # Cycles: 1 + 6 + 32 * (2 + 1) =
    # 1 set, 5 set + delay, 32 label + nop + jmp, repeat 3 times
    set(pins, 1)
    set(x, 2)                   [5]
    label("delay_high")
    nop()                       [29]
    jmp(x_dec, "delay_high")

    # Cycles: 1 + 1 + 6 + 32 * (30 + 1) = 1000
    nop()
    set(pins, 0)
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
    
    label("noperation")
    nop()
    jmp("noperation")
    # fmt: on

# Create the StateMachine with the blink_1hz program, outputting on Pin(25).
sm = rp2.StateMachine(0, blink_1hz, freq=500000, set_base=Pin(14), jmp_pin=Pin(13))

# Load the total pulse value into the TX FIFO then load into Y register.
sm.put(49)					# Total pulses of 50
sm.exec("pull()")			# Pull from TX FIFO to OSR
sm.exec("mov(y,osr)")		# Move from OSR to Y

# Start the StateMachine.
sm.active(1)


while True:
    time.sleep(1)
    #print(x)

sm.active(0)

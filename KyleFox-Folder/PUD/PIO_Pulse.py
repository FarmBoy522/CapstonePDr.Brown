# Creating a 200uS pulse with a wait of 10ms
# Loads the total pulse number of 50 (dec 49) into TX FIFO -> OSR -> Y Scratch
# Can start and stop State Machine as needed to do pulses

import time
from machine import Pin
import rp2

@rp2.asm_pio(set_init=rp2.PIO.OUT_HIGH, sideset_init=rp2.PIO.OUT_LOW)
def pulse_management():
    # Total Loop Label
    label("total_pulse")
    
    # Cycles: 1 + 6 + 32 * (2 + 1) = 117 cycles
    # 1 set, 5 set + delay, 32 label + nop + jmp, repeat 3 times
    set(pins, 0)				.side(1)
    set(x, 1)                   [5]
    label("delay_high")
    nop()                       [7]
    nop()                       [7]
    nop()                       [7]
    nop()                       [7]
    nop()                       [7]
    nop()                       [4]
    jmp(x_dec, "delay_high")

    # Cycles: 1 + 1 + 6 + 157 * (30 + 1) = 5115 cycles
    # 1 nop, 1 set, 5 set + delay, 157 label + nop + jmp, repeat 31 times
    nop()
    set(pins, 1)				.side(0)
    set(x, 30)                  [5]
    label("delay_low")
    nop()                       [7]
    nop()                       [7]
    nop()                       [7]
    nop()                       [7]
    nop()                       [7]
    jmp(x_dec, "delay_low")
    jmp(y_dec, "total_pulse")
    
    # End on nop to prevent continuious pulses
    label("noperation")
    nop()
    jmp("noperation")

# Create the StateMachine with the blink_1hz program, outputting on Pin(25).
sm = rp2.StateMachine(0, pulse_management, freq=500000, set_base=Pin(14), sideset_base=Pin(15))

# Load the total pulse value into the TX FIFO then load into Y register.
sm.put(49)					# Total pulses of 50
sm.exec("pull()")			# Pull from TX FIFO to OSR
sm.exec("mov(y,osr)")		# Move from OSR to Y

time.sleep(10)

# Start the StateMachine.
print("DATA NOW")
sm.active(1)
time.sleep(1)
sm.active(0)
print("Done")

# # Restart and Reset values to repeat a second time
# sm.restart()
# # Load the total pulse value into the TX FIFO then load into Y register.
# sm.put(49)					# Total pulses of 50
# sm.exec("pull()")			# Pull from TX FIFO to OSR
# sm.exec("mov(y,osr)")		# Move from OSR to Y
# sm.active(1)
# print("Done 2")
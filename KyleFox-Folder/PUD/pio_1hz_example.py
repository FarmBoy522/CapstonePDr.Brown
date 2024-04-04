# Example using PIO to blink an LED and raise an IRQ at 1Hz.
# Note: this does not work on Pico W because it uses Pin(25) for LED output.

# ruff: noqa: F821 - @asm_pio decorator adds names to function scope

import time
from machine import Pin
import rp2

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink_1hz():
    # fmt: off
    label("total_pulse")
    # Cycles: 1 + 1 + 6 + 32 * (30 + 1) = 1000
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


# Set doubling pin to high

# Create the StateMachine with the blink_1hz program, outputting on Pin(25).
sm = rp2.StateMachine(0, blink_1hz, freq=500000, set_base=Pin(14), jmp_pin=Pin(13))

# Set the IRQ handler to print the millisecond timestamp.
sm.put(49)
sm.exec("pull()")
sm.exec("mov(y,osr)")

# Start the StateMachine.
sm.active(1)


while True:
    time.sleep(1)
    #print(x)

sm.active(0)
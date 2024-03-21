import machine
import utime
import rp2

# Blink state machine program. Blinks LED at 10 Hz (with freq=2000)
# 2000 Hz / (20 cycles per instruction * 10 instructions) = 10 Hz
# Single pin (base pin) starts at output and logic low
@rp2.asm_pio(set_init=rp2.PIO.OUT_HIGH)
def blink():
    set(pins, 0)
    set(pins, 1) [31]
    nop() [31]
    nop() [31]
    nop() [31]
    nop() [31]
    nop() [31]
    nop() [31]
    nop() [31]
    nop() [31]
    nop() [31]
    nop() [31]
    nop() [31]
    nop() [31]
    nop() [31]
    nop() [31]
    nop() [31]
    nop() [31]
    nop() [31]
    nop() [31]
    nop() [31]
    set(pins, 0) [31]
    label("no-operations")
    nop() [31]
    nop() [31]
    nop() [31]
    nop() [31]
    nop() [31]
    jmp("no-operations")

# Init state machine with "blink" program
# (state machine 0, running at 2kHz, base pin is GP25 (LED))
sm = rp2.StateMachine(0, blink, freq=2000, set_base=machine.Pin(25))

# Continually start and stop state machine
utime.sleep(2)
while True:
    print("Starting state machine...")
    sm.active(1)
    utime.sleep(4)
    print("Stopping state machine...")
    sm.active(0)
    utime.sleep(1)
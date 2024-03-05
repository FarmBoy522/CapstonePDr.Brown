import rp2
import time

def state1(timeset, piosm, PinArray):
    smpulse = rp2.StateMachine(0, pulse, freq=500000, set_base=machine.Pin(14))
    #start charging
    time.sleep(600) # Wait 10min before checking ADC
    if voltage1.read_u16() > 100:
        pulse()
    else:
        time.sleep(60)
        fail += 1
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

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def pulse():
    set(pins, 0)
    set(pins, 1)
    set(pins, 0) [3]
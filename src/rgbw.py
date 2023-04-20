from machine import Pin
import utime

dataPIN = 4
latchPIN = 3
clockPIN = 2
blankPIN = 5

dataPIN=Pin(dataPIN, Pin.OUT)
latchPIN=Pin(latchPIN, Pin.OUT)
clockPIN=Pin(clockPIN, Pin.OUT)
blankPIN=Pin(blankPIN, Pin.OUT)


def shift_update(input,data,clock,latch):
    #put latch down to start data sending
    blankPIN.value(1)
    blankPIN.value(0)
    clock.value(0)
    latch.value(1)
    latch.value(0)
  
    #load data in reverse order
    for i in range(len(input) - 1, -1, -1):
        clock.value(0)
        data.value(int(input[i]))
        clock.value(1)


    #put latch up to store data on register
    clock.value(0)
    latch.value(1)
    latch.value(0)


bit_string="10000000000000000000000000000000"
for i in range(len(bit_string)):
    shift_update(bit_string,dataPIN,clockPIN,latchPIN)
    bit_string = str(0) + bit_string[:-1]
    utime.sleep(0.2)


shift_update("0000000000000000",dataPIN,clockPIN,latchPIN)
shift_update("1000"*24,dataPIN,clockPIN,latchPIN)

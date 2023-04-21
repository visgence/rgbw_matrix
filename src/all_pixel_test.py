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

ROWS=6
COLS=4

RED="0001"
BLUE="0100"
GREEN="0010"
WHITE="1000"
OFF="0000"

PIXEL_BUFFER=[["0000" for y in range(ROWS)] for x in range(COLS)]

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


def write_screen():
    bit_string = ""
    for x in range(COLS):
        for y in range(ROWS):
            # print(PIXEL_BUFFER[x][y])
            bit_string += str(PIXEL_BUFFER[x][y])
    print(bit_string)
    shift_update(bit_string,dataPIN,clockPIN,latchPIN)

write_screen()

#TODO: cycle solid colors
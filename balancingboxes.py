from microbit import *

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

FL = pin14
BL = pin13
FR = pin12
BR = pin15

on = 511
off = 1023

def stop(time):
    display.clear()
    FL.write_analog(off)
    BL.write_analog(off)
    FR.write_analog(off)
    BR.write_analog(off)
    sleep(time)

def forward(time):
    display.show(Image.ARROW_N)
    FL.write_analog(on)
    BL.write_analog(off)
    FR.write_analog(on)
    BR.write_analog(off)
    sleep(time)

stop(1)

while True:
    display.show(Image.HAPPY)
    if button_a.was_pressed():
        sleep(10000)
        forward(5000)
        stop(1)
    else:
        sleep(1)
        

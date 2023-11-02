# Imports go at the top
from microbit import *
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text

def temperature1():
    i=temperature()
    if i>=25:
        pin16.write_digital(1)
    else:
        pin16.write_digital(0)
def light_level1():
    o=display.read_light_level()
    s=1023-o
    if o<=150:
        pin1.write_analog(s)
    elif o>150:
        pin1.write_analog(0)
def tempreture_and_light_level():
    j=display.read_light_level()
    b=temperature()
    sleep(2000)
    b=str(b)
    j=str(j)
    add_text(0, 0, j)
    add_text(0, 1, b)
    

while True:
    motion = pin2.read_digital()
    if motion == 1:
        light_level1()
        temperature1()
    tempreture_and_light_level()
        
        
        

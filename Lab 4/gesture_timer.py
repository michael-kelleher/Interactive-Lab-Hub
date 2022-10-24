# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
from adafruit_apds9960.apds9960 import APDS9960
import qwiic_oled_display
import time
from threading import Thread

myOLED = qwiic_oled_display.QwiicOledDisplay()
myOLED.begin()
myOLED.clear(myOLED.PAGE)
myOLED.set_font_type(2)
myOLED.set_cursor(0,0)

myOLED.display()

i2c = board.I2C()

apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = True

def display(ctime):
    myOLED.clear(myOLED.PAGE)
    minutes = ctime // 60
    seconds = ctime % 60
    myOLED.set_cursor(0,0)
    ptime = f'{minutes:02}' + ":" + f'{seconds:02}'
    myOLED.print(ptime)
    myOLED.display()



ctime = 600
display(ctime)
gesture = apds.gesture()
while gesture != 0x03:
    display(ctime)
    while gesture == 0:
        gesture = apds.gesture()
    if gesture == 0x02:
        ctime += 60
        
        print("up")
    elif gesture == 0x01:
        ctime -= 60
        
        print("down")
    elif gesture == 0x03:
        print("left")
        break
    elif gesture == 0x04:
        print("right")
    gesture = 0
    
print("hi")
while True:
    print(ctime)
    display(ctime)
    ctime = ctime - 1
    time.sleep(1)
    
    


    

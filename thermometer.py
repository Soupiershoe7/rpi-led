import board
import neopixel
import time
import random

pixels = neopixel.NeoPixel(board.D18, 20)

def thermometer (T):
    for i in range (int(T) - 90):
        pixels[i] = (10,0,0)

randnum = random.randint (90,110)

for i in range (10):
    temp= (randnum)
    print (randnum)
    thermometer (temp)
    time.sleep (1)

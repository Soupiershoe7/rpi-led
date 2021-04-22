import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 20)

def thermometer (T):
    for i in range (int(T) - 90):
        pixels[i] = (10,0,0)


temp= 97.56

thermometer (temp)

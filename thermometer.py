import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 20)

temp= 97.56

for i in range (int(temp) - 90):
    pixels[i] = (10,0,0)

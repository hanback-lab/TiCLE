import ticle
import time
import random

pl = ticle.PixelLed(7)

while True:
    for w in range(1,5+1):
        for i in range(10):
            if i >= 5-w and i <= 4+w:
                pl[i] = (255,0,0)
            else:
                pl[i] = (0,0,0)
        pl.write()
        time.sleep(0.1)
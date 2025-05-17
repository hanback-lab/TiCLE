import ticle
import time
import random

pl = ticle.PixelLed(7, 10)

loc = 0
constant = 1
while True:
    for i in range(10):
        if loc == i:
            pl[i] = (255,0,0)
        else:
            pl[i] = (0,0,0)
    if loc == 9:
        constant = -1
    elif loc == 0:
        constant = 1
    loc+=constant
    pl.update()
    time.sleep(0.1)
        

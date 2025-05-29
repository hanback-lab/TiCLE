import ticle
import time

pl = ticle.PixelLed(7, 10)

for j in range(255):
    for i in range(10):
        pl[i] = (j, 0, 0)
    pl.write()
    time.sleep(0.01)
while True:
    for j in range(255):
        for i in range(10):
            pl[i] = (255-j, j, 0)
        pl.write()
        time.sleep(0.01)
    for j in range(255):
        for i in range(10):
            pl[i] = (0, 255-j, j)
        pl.write()
        time.sleep(0.01)
    for j in range(255):
        for i in range(10):
            pl[i] = (j, 0, 255-j)
        pl.write()
        time.sleep(0.01)
        
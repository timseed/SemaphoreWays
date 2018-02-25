#!/usr/bin/env python3

from Lock import Lock
from time import sleep

try:
    lock = Lock("Worker")
    while not lock.acquire():
        print("Fun2 No Lock available")
        sleep(1)
    else:
        print("Got Lock")
        for loop in range(1, 5):
            print("Fun2 Working {}".format(loop))
            sleep(1)
finally:
    lock.release()

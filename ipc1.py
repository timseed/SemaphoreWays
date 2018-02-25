#!/usr/bin/env python3

from Lock import Lock
from time import sleep

# Usage
try:
    lock = Lock("Worker")
    lock.acquire()
    print("fun1 starting")
    for loop in range(1, 5):
        print("Fun1 Working {}".format(loop))
        sleep(1)
    print("fun1 finished")
finally:
    print("Releasing Lock")
    lock.release()
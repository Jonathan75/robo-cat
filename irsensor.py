import RPi.GPIO as io
import time

io.setmode(io.BCM)

sensor= 18

io.setmode(io.BCM)
io.setup(sensor, io.IN, pull_up_down=io.PUD_DOWN)

current = io.input(sensor)
previous = current

def changeDetected(current):
    if current == 0:
        objectDetected()
    else:
        objectOutOfRange()
    
def objectDetected():
    print('gonna hit something')

def objectOutOfRange():
    print('okay now')

def detectChange():
    current = io.input(sensor)
    print(current)
    if current != previous:
        return current
    else:
        return False

import RPi.GPIO as io
import time

io.setmode(io.BCM)

right_1 = 4
right_2 = 17
left_1 = 27
left_2 = 22

sensor = 18

io.setup(right_1, io.OUT)
io.setup(right_2, io.OUT)
io.setup(left_1, io.OUT)
io.setup(left_2, io.OUT)

io.setup(sensor, io.IN, pull_up_down=io.PUD_DOWN)

def forward():
    print('forward')
    io.output(right_1, False)
    io.output(right_2, True)
    io.output(left_1, False)
    io.output(left_2, True)

def stop():
    print('stop')
    io.output(right_1, False)
    io.output(right_2, False)
    io.output(left_1, False)
    io.output(left_2, False)

# current = io.input(sensor)
# previous = current

def read_sensor():
    return io.input(sensor)
    
def should_stop():
    return not(read_sensor())
    # current = io.input(sensor)
    # global previous
    print(read_sensor())
    #if current != previous:
    #    previous = current
    #    return True
    #return False

forward()
print('start')

try:
    while True:
        time.sleep(1)
        if should_stop():
            stop()
        else:
            forward()

except KeyboardInterrupt:
    stop()

finally:
    io.cleanup()

import RPi.GPIO as io
io.setmode(io.BCM)
import pin_setup



# TODO: Make this work
##def set(property, value):
##    try:
##        f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
##        f.write(value)
##        f.close()	
##    except:
##        print("Error writing to: " + property + " value: " + value)
 
# set("delayed", "0")
# set("mode", "pwm")
# set("frequency", "500")
# set("active", "1")


#class motor:
#    def __init__(self):
left_1 = 4
left_2 = 17
right_1 = 27
right_2 = 22
io.setup(right_1, io.OUT)
io.setup(right_2, io.OUT)
io.setup(left_1, io.OUT)
io.setup(left_2, io.OUT)
print('motor loaded')
    
def forward():
    print('forward')
    io.output(right_1, 100)
    io.output(right_2, 0)

    io.output(left_1, False)
    io.output(left_2, True)

def stop():
    print('stop')
    io.output(right_1, False)
    io.output(right_2, False)
    io.output(left_1, False)
    io.output(left_2, False)

def backward():
    io.output(right_1, True)
    io.output(right_2, False)
    io.output(left_1, True)
    io.output(left_2, False)


def backwardLeft():
    io.output(right_1, True)
    io.output(right_2, False)
    io.output(left_1, False)
    io.output(left_2, False)

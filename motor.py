import RPi.GPIO as io
io.setmode(io.BCM)

right_1 = 4
right_2 = 17
left_1 = 27
left_2 = 22

io.setup(right_1, io.OUT)
io.setup(right_2, io.OUT)
io.setup(left_1, io.OUT)
io.setup(left_2, io.OUT)

# TODO: Make this work
def set(property, value):
    try:
        f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
        f.write(value)
        f.close()	
    except:
        print("Error writing to: " + property + " value: " + value)
 
# set("delayed", "0")
# set("mode", "pwm")
# set("frequency", "500")
# set("active", "1")

def forward():
    io.output(right_1, True)    
    io.output(right_2, False)
    io.output(left_1, True)
    io.output(left_2, False)

def back():
    io.output(right_1, False)
    io.output(right_2, True)
    io.output(left_1, False)
    io.output(left_2, True)

def stop():
    io.output(right_1, False)
    io.output(right_2, False)
    io.output(left_1, False)
    io.output(left_2, False)

while True:
    cmd = raw_input("f: forward, b: back >> ")
    direction = cmd[0]
    if direction == "f":
        forward()
    elif direction == "b": 
        back()
    else:
        stop()
    try:
        pass
        # speed = int(cmd[1]) * 11
        # set("duty", str(speed))
    except KeyboardInterrupt: 
        io.cleanup() 


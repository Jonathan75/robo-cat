import RPi.GPIO as io
io.setmode(io.BCM)
io.cleanup()

right_1 = 4
right_2 = 17
left_1 = 27
left_2 = 22

io.setup(right_1, io.OUT)
io.setup(right_2, io.OUT)
io.setup(left_1, io.OUT)
io.setup(left_2, io.OUT)

def set(property, value):
    try:
        f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
        f.write(value)
        f.close()	
    except:
        print("Error writing to: " + property + " value: " + value)
 
set("delayed", "0")
set("mode", "pwm")
set("frequency", "500")
set("active", "1")

def clockwise():
    io.output(right_1, True)    
    io.output(right_2, False)
    io.output(left_1, True)
    io.output(left_2, False)

def counter_clockwise():
    io.output(right_1, False)
    io.output(right_2, True)
    io.output(left_1, False)
    io.output(left_2, True)

clockwise()

while True:
    cmd = raw_input("Command, f/r 0..9, E.g. f5 :")
    direction = cmd[0]
    if direction == "f":
        clockwise()
    else: 
        counter_clockwise()
    try:
        #speed = int(cmd[1]) * 11
        set("duty", "99")
    except: 
        pass

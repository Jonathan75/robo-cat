import motor
import irsensor

def objectDetected():
    print('here')
    motor.stop()

motor.forward()
state = False

while True:
    #state = irsensor.detectChange()
    if state==0:
        motor.stop()
    try:
        pass
    except KeyboardInterrupt:
        motor.stop()
        io.cleanup()

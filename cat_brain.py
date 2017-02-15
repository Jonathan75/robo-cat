import RPi.GPIO as io
import time
import motor
import range_sensor
io.setmode(io.BCM)
print('start')

try:
    while True:
        time.sleep(0.1)
        if range_sensor.too_close():
            print('backward')
            motor.backward()
            time.sleep(1)
        else:
            print('forward')
            motor.forward()

except KeyboardInterrupt:
    motor.stop()

finally:
    io.cleanup()

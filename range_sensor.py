import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24
MIN_DISTANCE = 20

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def triger():
  #print "ping"
  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)


def read_distance():
  GPIO.output(TRIG, False)
  #print "Waiting For Sensor To Settle"
  time.sleep(.5)

  triger()
  pulse_start = 0
  while GPIO.input(ECHO)==0:
    pulse_start = time.time()

  # triger()
  
  while GPIO.input(ECHO)==1:
    pulse_end = time.time()
    #print "pong"
    
  
  pulse_duration = pulse_end - pulse_start
  print pulse_duration

  distance = pulse_duration * 17150

  return round(distance, 2)

def too_close():
##  return False
  return read_distance() < MIN_DISTANCE


##try:
##  GPIO.setup(TRIG,GPIO.OUT)
##  GPIO.setup(ECHO,GPIO.IN)
##  while(True):
##    triger()
##    time.sleep(1)
##    
##    print "Distance:",read_distance(),"cm"
##    print "Too Close:",too_close()
##
##except KeyboardInterrupt:
##  #triger()
##  GPIO.output(TRIG, False)
##
##finally:
##    GPIO.cleanup()

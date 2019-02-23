# External module imports
import RPi.GPIO as GPIO
import time

# ********** initiate System *****************
# The following program will control the servo making it move
# to its neutral position (90 degrees), wait 1 second and then move to its 0 degrees,
# wait 1 second and finally move to its 180 degrees.

# setup pin number based off board numbering
GPIO.setmode(GPIO.BOARD)

# setup pin 12 to be an output pin for PWM
GPIO.setup(12, GPIO.OUT)

# PWM instance associated GPIO Pin 12 at 50Hz
p = GPIO.PWM(12, 25)

p.start(7.5)


# ********************* Main Code *****************
try:
    while True:
        p.ChangeDutyCycle(2.5)
        time.sleep(5)
        p.ChangeDutyCycle(5)
        time.sleep(5)
        p.ChangeDutyCycle(7.5)
        print("repeat")

except KeyboardInterrupt:
    print("ctr-c pressed\n")
    p.ChangeDutyCycle(7.5)
    p.stop()
    GPIO.cleanup()


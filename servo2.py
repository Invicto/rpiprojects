from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

p = GPIO.PWM(11, 50)  # channel=12 frequency=50Hz
p.start(1)
sleep(1)
p.ChangeDutyCycle(5)
sleep(1)
p.stop()
GPIO.cleanup()

from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setwarnings(False)
p = GPIO.PWM(12, 50)  # channel=12 frequency=50Hz

#full left
print "full left"
p.start(5)
sleep(1)
p.ChangeDutyCycle(12)
sleep(1)
p.stop()
GPIO.cleanup()

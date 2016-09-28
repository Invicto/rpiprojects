from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)  # channel=12 frequency=50Hz

#full left
print "full left"
p.start(1)
sleep(1)
p.ChangeDutyCycle(1)
sleep(1)
p.ChangeDutyCycle(2)
sleep(1)
p.ChangeDutyCycle(3)
sleep(1)
p.ChangeDutyCycle(4)
sleep(1)
p.ChangeDutyCycle(5)
sleep(1)
p.ChangeDutyCycle(6)
sleep(1)
p.ChangeDutyCycle(7)
sleep(1)
p.ChangeDutyCycle(8)
sleep(1)
p.ChangeDutyCycle(9)
sleep(1)
p.ChangeDutyCycle(10)
sleep(1)
p.stop()
GPIO.cleanup()

# import RPi.GPIO as GPIO
import time

motor = 23
water_motor = 24
motor_rev = 25

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(motor, GPIO.OUT)
# GPIO.setup(water_motor, GPIO.OUT)
# GPIO.setup(motor_rev, GPIO.OUT)


def RunMotor(running_time) -> None:
    print("Motor Started")
    # GPIO.output(motor, GPIO.LOW)
    time.sleep(running_time)
    # GPIO.output(motor, GPIO.HIGH)
    print("Motor Stopped")


def RunMotorReverse(running_time) -> None:
    print("Motor Reversed")
    # GPIO.output(motor, GPIO.LOW)
    time.sleep(running_time)
    # GPIO.output(motor, GPIO.HIGH)
    print("Motor Reached to initial position")

def RunWaterPump(running_time) -> None:
    print("Water Pump Started")
    # GPIO.output(motor, GPIO.LOW)
    time.sleep(running_time)
    # GPIO.output(motor, GPIO.HIGH)
    print("Water Pump Stopped")



# delay_time = 2
# RunWaterPump(delay_time)



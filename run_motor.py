import time

def RunMotor(running_time) -> None:
    print("Motor Started")
    time.sleep(running_time)
    print("Motor Stopped")


def RunMotorReverse(running_time) -> None:
    print("Motor Reversed")
    time.sleep(running_time)
    print("Motor Reached to initial position")

def RunWaterPump(running_time) -> None:
    print("Water Pump Started")
    time.sleep(running_time)
    print("Water Pump Stopped")



# delay_time = 2
# RunWaterPump(delay_time)



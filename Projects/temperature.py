import grovepi
import time

while True:
        # Read distance value from Ultrasonic
        temp = grovepi.temperature()

        print(temp)
        time.sleep(1)

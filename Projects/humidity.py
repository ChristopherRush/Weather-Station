import grovepi
import time

while True:
        # Read distance value from Ultrasonic
        humid = grovepi.humidity()

        print(humid)
        time.sleep(1)

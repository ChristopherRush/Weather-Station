import grovepi
import time

vane = 0


while True:
    direction = analogRead(vane)
    print direction
    time.sleep(1)

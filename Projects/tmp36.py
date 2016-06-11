import grovepi
import time

sensor 1

grovepi.pinMode(sensor, "INPUT")

while True:
    temp = grovepi.analogRead(sensor)
    print temp
    time.sleep(1)

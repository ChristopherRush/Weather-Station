import grovepi
import time

sensor = 1

grovepi.pinMode(sensor, "INPUT")

while True:
    temp = grovepi.analogRead(sensor)
    volt = temp * 5.0 / 1024
    number = (volt - 0.5) * 100
    number = round(t, 2)
    print (number)
    time.sleep(1)

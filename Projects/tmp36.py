import grovepi
import time

sensor = 1

grovepi.pinMode(sensor, "INPUT")

while True:
    temp = grovepi.analogRead(sensor)
    volt = temp * 3.3 / 1024
    number = (volt - 0.5) * 100
    number = round(number, 2)
    print (number)
    time.sleep(1)

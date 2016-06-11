import grovepi
import time

sensor = 1

grovepi.pinMode(sensor, "INPUT")

while True:
    temp = grovepi.analogRead(sensor)
    volts = temp * 5.0 / 1024
    t = (volts - 0.5) * 100
    t = round(t, 2)
    print (t)
    time.sleep(1)

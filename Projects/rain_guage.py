import grovepi
import time, datetime

guage = 3

pinMode(guage, "INPUT")

while True:
    rain_status = digitalRead(guage)
    if rain_status:
        print ("ON")
    else:
        print ("OFF")

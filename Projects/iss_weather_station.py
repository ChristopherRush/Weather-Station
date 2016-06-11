import time
import grovepi
from ISStreamer.Streamer import Streamer

streamer = Streamer(bucket_name="weather", bucket_key="63CXMKAEQVFR", access_key="NXNfXQSbMgvPPSqD0gEEr0zX3OHeam2r")

sensor = 1
vane = 0

grovepi.pinMode(sensor, "INPUT")
grovepi.pinMode(vane, "INPUT")

while True:
    temp = grovepi.analogRead(sensor)
    volt = temp * 3.3 / 1024
    number = (volt - 0.5) * 100
    number = round(number, 2)
    print (number)
    streamer.log("Temperature", number)
    #time.sleep(1)

    speed = grovepi.anenometerRead()
    streamer.log("Wind Speed", speed)
    print (speed)
    #time.sleep(1)

    direction = grovepi.analogRead(vane)
    #print direction
    if direction == 234:
        streamer.log("Wind Direction", "North")
        #print "North"
    elif direction == 133:
        streamer.log("Wind Direction", "North West")
        #print "North West"
    elif direction == 76:
        streamer.log("Wind Direction", "West")
        #print "West"
    elif direction == 389:
        streamer.log("Wind Direction", "South West")
        #print "South West"
    elif direction == 734:
        streamer.log("Wind Direction", "South")
        #print "South"
    elif direction == 838:
        streamer.log("Wind Direction", "South East")
        #print "South East"
    elif direction == 930:
        streamer.log("Wind Direction", "East")
        #print "East"
    elif direction == 559:
        streamer.log("Wind Direction", "North East")
        #print "North East"
    #time.sleep(1)

    streamer.flush()
    time.sleep(30)

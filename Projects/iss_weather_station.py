import time
from time import strftime
import grovepi
from ISStreamer.Streamer import Streamer

streamer = Streamer(bucket_name="weather", bucket_key="63CXMKAEQVFR", access_key="NXNfXQSbMgvPPSqD0gEEr0zX3OHeam2r")

sensor = 1
vane = 0


grovepi.pinMode(sensor, "INPUT")
grovepi.pinMode(vane, "INPUT")

speedlist = []
resetvalue = 0
average = 0

while True:

    streamer.log(":house: Location", "Preston, Lancashire :flag_gb:")

    print(strftime("%H:%M"))
    streamer.log(":clock3: Updated Time", strftime("%H:%M"))

    temp = grovepi.analogRead(sensor)
    volt = temp * 5.0 / 1024
    number = (volt - 0.5) * 100
    number = round(number, 2)
    print (number)
    streamer.log(":thermometer: Temperature", number)
    time.sleep(1)



    direction = grovepi.analogRead(vane)
    print direction
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
    time.sleep(1)

    speed = grovepi.anenometerRead()
    streamer.log(":wind_blowing_face: Wind Speed", speed)
    speedlist.append(speed)
    average = sum(speedlist) / float(len(speedlist))
    print round(average, 2)

    resetvalue += 1
    if resetvalue == 10:
        resetvalue = 0
        speedlist = []
    time.sleep(1)

    inches = grovepi.rain_gauge()
    print (inches)
    streamer.log(":droplet: Rain mm", inches)
    time.sleep(1)

    streamer.flush()

    if int(strftime("%H")) > 06 and int(strftime("%H")) < 22:
        time.sleep(60)
    else:
        time.sleep(3600)

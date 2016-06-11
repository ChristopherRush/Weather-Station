import grovepi
import time

vane = 0


while True:
    direction = grovepi.analogRead(vane)
    print direction
    if direction == 235:
        print "North"
    elif direction == 133:
        print "North West"
    elif direction == 76:
        print "West"
    elif direction == 389:
        print "South West"
    elif direction == 734:
        print "South"
    elif direction == 837:
        print "South East"
    elif direction == 929:
        print "East"
    elif direction == 559:
        print "North East"
    time.sleep(0.5)

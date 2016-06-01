import grovepi

# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND

while True:
    try:
        # Read distance value from Ultrasonic
        print(grovepi.anenometerRead(2))

    except TypeError:
        print ("Error")
    except IOError:
        print ("Error")

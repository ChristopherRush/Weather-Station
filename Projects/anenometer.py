import grovepi

# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND

while True:
    try:
        # Read distance value from Ultrasonic
        print(grovepi.anenometerRead())

    except TypeError:
        print ("Error 1")
    except IOError:
        print ("Error 2")

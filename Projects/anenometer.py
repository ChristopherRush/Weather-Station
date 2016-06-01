import grovepi

# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND
anenometerPin = 2

while True:
    try:
        # Read distance value from Ultrasonic
        print(grovepi.anenometerRead(anenometerPin))

    except TypeError:
        print ("Error")
    except IOError:
        print ("Error")

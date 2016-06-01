import time
import grovepi

# Connect the TMP36 Temperature Sensor to analog port A1

sensor = 1

while True:
    try:
        temp = grovepi.temp36(sensor)
        round(temp,2)
        print("temp =", temp)
        time.sleep(.5)

    except KeyboardInterrupt:
        break
    except IOError:
        print ("Error")

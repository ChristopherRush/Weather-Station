import grovepi
import time, datetime




while True:
    inches = grovepi.rain_gauge()
    print (inches)
    time.sleep(1)

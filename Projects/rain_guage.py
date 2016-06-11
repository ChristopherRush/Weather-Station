import grovepi
import time, datetime

gauge = 3



while True:
    inches = grovepi.rain_gauge(gauge)
    print (inches)
    time.sleep(1)

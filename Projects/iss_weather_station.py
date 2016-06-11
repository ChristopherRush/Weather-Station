import time
import grovepi
from ISStreamer.Streamer import Streamer

streamer = Streamer(bucket_name="weather", bucket_key="[63CXMKAEQVFR]", access_key="[NXNfXQSbMgvPPSqD0gEEr0zX3OHeam2r]")

sensor = 1

while True:
    temp = grovepi.temp36(sensor)
    temp = round(temp,2)
    streamer.log("Temperature", temp)
    time.sleep(30)

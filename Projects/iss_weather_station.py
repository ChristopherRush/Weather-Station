import time
import grovepi
from ISStreamer.Streamer import Streamer

streamer = Streamer(bucket_name="weather", bucket_key="[TPA5P4TVJA5J]", access_key="[NXNfXQSbMgvPPSqD0gEEr0zX3OHeam2r]")

sensor = 1

while True:
    temp = grovepi.temp36(sensor)
    temp = round(temp,2)
    streamer.log("temp", temp)
    time.sleep(30)

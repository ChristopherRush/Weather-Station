import time
import grovepi
from ISStreamer.Streamer import Streamer

streamer = Streamer(bucket_name="weather test", bucket_key="[TPA5P4TVJA5J]", access_key="[EaWzZnoEuilOAxVi8tz3USRhW6ZnclWW]")

sensor = 1

while True:
    temp = grovepi.temp36(sensor)
    temp = round(temp,2)
    streamer.log("Temperature", temp)
    time.sleep(30)

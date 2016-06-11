import grovepi
import time
vane = 0

pinMode (vane, "INPUT")

while True:
    direction = analogRead(vane)
    print direction
    time.sleep(1)

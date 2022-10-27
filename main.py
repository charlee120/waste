import database as db
import load
import distance
import time
while True:
  d = distance.distance()
  w = load.loop()
  db.database(d,w)
  print("data pushed")
  time.sleep(2)
  
  
from flask import Flask, jsonify
from datetime import datetime, date
import calendar
app = Flask(__name__)

@app.route("/api/current")
def currentTime():
  t = datetime.now()
  
  if calendar.isleap(t.year):
    days = 366
  else:
    days = 365
  
  blocks = days * 3
  d0 = date(t.year, 1, 1)
  d1 = date(t.year, t.month, t.day)
  delta = d1 - d0
  dayblocks = delta.days * 3
  count = blocks - dayblocks
  
  if t.hour < 8:
    count = blocks - dayblocks
  elif t.hour < 16:
    count = blocks - (dayblocks + 1)
  else:
    count = blocks - (dayblocks + 2)

  time = {'time' : count}
  return jsonify(**time)

if __name__ == "__main__":
  app.run()

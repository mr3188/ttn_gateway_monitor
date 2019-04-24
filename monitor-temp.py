# monitor-temp.py
import sys
import os, time, urllib
import paho.mqtt.publish as publish
import Adafruit_DHT
import json

def measure_temp():
      temp = os.popen("vcgencmd measure_temp").readline()
      temp = temp.replace("temp=","")
      temp = temp.replace("'C","")
      fTemp = float(temp)
      print(temp)
      humidity, box_temp = Adafruit_DHT.read_retry(11, 23)

      data={}
      data["cpu_temp"]=fTemp
      data["box_temp"]=box_temp
      data["humidity"]=humidity

      print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(box_temp, humidity))
      payload=json.dumps(data)
      publish.single("ttn-gateway/temp", payload=payload, hostname="192.168.1.31", client_id="ttn-gateway")
while True:
      measure_temp()
      time.sleep(1800)






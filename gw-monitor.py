# gw-monitor.py
import sys
import os, time, urllib
import ConfigParser
import paho.mqtt.publish as publish
import Adafruit_DHT
import json
import socket



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
     
      try:
            publish.single(hostname+"/status/temp", payload=payload, hostname=mqtt_server, client_id=hostname)
      except:
            print("unable to publish mqtt message", sys.exc_info()[0])

def send_state(state="running"):
      
      try:
            publish.single(hostname+"/status/state", payload=state, retain=True, hostname=mqtt_server, client_id=hostname, )
      except:
            print("unable to publish mqtt message", sys.exc_info()[0])



path = os.path.dirname(os.path.abspath(__file__))
hostname=socket.gethostname()

# configuration
config = ConfigParser.ConfigParser()

try:
      configFilePath= path + '/getBandwidth.conf'
      config.read(configFilePath)

      mqtt_server=config.get("mqtt", "mqtt_server")
      DHT_Pin=config.getint("DHT11", "DHT_Pin")
      
except:
      send_state("Error reading config file ")
      exit(-1)


while True:
      measure_temp()
      time.sleep(60*5)






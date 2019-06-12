# ttn_gateway_monitor
Script to monitor Raspberry Pi TTN gateway

This script must be run as root.

To launch gateway monitor at startup add the following line to /etc/rc.local (change the script path as needed)

(sleep 10; python /home/ttn/adminTools/ttn_gateway_monitor/gw-monitor.py)&

There must be a config file in the same script directory 

gw-monitor.conf

[mqtt]
mqtt_server = <server_name>

[DHT11]
DHT_pin = 23


# ttn_gateway_monitor
Scripts to monitor Raspberry Pi TTN gateway


Launch gateway monitor at startup add the following line to /etc/rc.local (change the script path as needed)

(sleep 10; python /home/ttn/adminTools/ttn_gateway_monitor/gw-monitor.py)&

There must be a config file in the same script directory 

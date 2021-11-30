import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import threading
import sys
import time

if __name__ == '__main__':
        
    topic = 'MulpubSameTop/Test'
    hostname = 'mqtt.eclipse.org'

    while True:
      msg = subscribe.simple(topic, qos = 0, msg_count = 1, retained = False, hostname = hostname, keepalive = 60, client_id = "", protocol = mqtt.MQTTv311, port = 1883) #default port 1883
      print(msg)
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import threading
import sys
import time

class myThread(threading.Thread):

    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)

def act_pub(topic, msg, hostname, port, qos, keepalive, transport):

    for i in range(10):
        msg = '{} iter {}'.format(msg, i+1)
        publish.single(topic, msg, hostname=hostname,port=port, qos=qos, keepalive=keepalive, transport=transport)
        time.sleep(10)

if __name__ == '__main__':
        
    topic = 'MulpubSameTop/Test'
    msg = 'Multiple Publisher send to same Topic Test'
    hostname = 'mqtt.eclipse.org'
    port = 1883
    qos = 2
    keepalive = 60
    transport = 'tcp'

    pub_num = int(sys.argv[1])
    pub_list = list()

    # create multiple publisher by thread
    for i in range(pub_num):
        msg = 'Thread {}: {}'.format(i+1, msg)
        tmp_pub = myThread(act_pub, [topic, msg, hostname, port, qos, keepalive, transport])
        pub_list.append(tmp_pub)

    # start publish
    for pub in pub_list:
        pub.start()

    # end publish
    for pub in pub_list:
        pub.join()
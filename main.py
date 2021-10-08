from os import sep
import paho.mqtt.client as mqtt
import time
import threading
import random
import config

def onConnect(client, userdata, flags_dict, result):
    print('onConnect')
def onSubscribe(client, userdata, mid, granted_qos):
    print('onSubscribe')
def onDisconnect(client, userdata, rc):
    print('onDisconnect')
def onMessage(client, userdata, message):
    print('message with title ',message.topic,': ', str(message.payload.decode('utf-8')), sep='')

def publisher(t, i):
    while True:
        #any value for publishing e.g: sensor value.
        #type of value can be specified with topic
        #e.g: if topic == 'lightSensor': publish light sensor value
        client.publish(t, str(random.randrange(10)))

        if i < 0: break
        else: time.sleep(i)


if __name__ == '__main__':
    
    broker='192.168.1.33'
    client= mqtt.Client('arhalap')
    client.on_connect= onConnect
    client.on_disconnect= onDisconnect
    client.on_message= onMessage
    client.on_subscribe= onSubscribe

    client.loop_start()

    client.connect(broker)
    time.sleep(1)
    while True:
        command= input()
        if command == 'sub':
            topic= input('topic: ')
            client.subscribe(topic)
        elif command == 'pub':
            topic= input('topic: ')
            interval= int(input('interval: '))
            t= threading.Thread(target=publisher, args=(topic, interval), daemon= True)
            t.start()
        elif command == 'quit': break

    client.disconnect()
    client.loop_stop()

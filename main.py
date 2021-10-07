from os import sep
import paho.mqtt.client as mqtt
import time

def onConnect(client, userdata, flags_dict, result):
    print('onConnect')
def onSubscribe(client, userdata, mid, granted_qos):
    print('onSubscribe')
def onDisconnect(client, userdata, rc):
    print('onDisconnect')
def onMessage(client, userdata, message):
    print('message with title ',message.topic,': ', str(message.payload.decode('utf-8')), sep='')


broker='192.168.1.33'

client= mqtt.Client('arhaLap')
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
        message= input('message: ')
        client.publish(topic, message)
    elif command == 'quit': break
    

client.disconnect()
client.loop_stop()

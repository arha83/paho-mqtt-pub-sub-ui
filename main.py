import paho.mqtt.client as mqtt
import time


def onConnect(client, userdata, flags_dict, result):
    print('onConnect')
def onSubscribe(client, userdata, mid, granted_qos):
    print('onSubscribe')
def onDisconnect(client, userdata, rc):
    print('onDisconnect')
def onMessage(client, userdata, message):
    print('onMessage')


client= mqtt.Client(client_id='arhaLap')
client.on_connect    = onConnect
client.on_disconnect = onDisconnect
client.on_message    = onMessage
client.on_subscribe  = onMessage


client.connect('192.168.1.33')
time.sleep(5)
client.disconnect()

import paho.mqtt.client as mqtt
import time


def onConnect(client, userdata, flags_dict, result):
    print('onConnect')
def onSubscribe(client, userdata, mid, granted_qos):
    print('onSubscribe')
def onDisconnect(client, userdata, rc):
    print('onDisconnect')
def onMessage(client, userdata, message):
    print('onMessage', str(message.payload.decode('utf-8')))


client= mqtt.Client('arhaLap')
client.on_connect= onConnect
client.on_disconnect= onDisconnect
client.on_message= onMessage
client.on_subscribe= onSubscribe

client.loop_start()

client.connect('192.168.1.33')
time.sleep(1)
client.subscribe('atitle')
time.sleep(1)
client.publish('atitle', payload='Is this working?')
time.sleep(1)
client.disconnect()

client.loop_stop()

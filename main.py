import paho.mqtt.client as mqtt
import time


def onConnect(client, userdata, flags_dict, result):
    print('connected...?!', type(result))
def onSubscribe(client, userdata, mid, granted_qos):
    pass
def onDisconnect(client, userdata, rc):
    print('disconnecting')
def onMessage(client, userdata, message):
    pass


client= mqtt.Client(client_id='arhaLap')
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
client.on_subscribe  = subscribed

print('Connecting')
client.connect('192.168.1.33')
print('Sleeping')
time.sleep(5)
print('disconnecting')
client.disconnect()

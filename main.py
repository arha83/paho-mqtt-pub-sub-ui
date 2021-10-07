import paho.mqtt.client as mqtt


def onConnect(client, userdata, flags_dict, result):
    pass
def onSubscribe(client, userdata, mid, granted_qos):
    pass
def onDisconnect(client, userdata, rc):
    pass
def onMessage(client, userdata, message):
    pass


client= mqtt.Client(client_id='arhaLap')


client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
client.on_subscribe  = subscribed

import paho.mqtt.client as mqtt
import json
import datetime

def time_now():
    return datetime.datetime.now().strftime('%H:%M:%S.%f')

# MQTT client to connect to the bus
mqtt_client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    mqtt_client.subscribe('#') # subscribe to all messages

# Process a message as it arrives
def on_message(client, userdata, msg):
        if len(msg.payload) > 0:
            print '[{}] - {}: {}'.format(time_now(), msg.topic, msg.payload)
        else:
            print '[{}] - {}'.format(time_now(), msg.topic)

mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect('localhost', 9898)
mqtt_client.loop_forever()

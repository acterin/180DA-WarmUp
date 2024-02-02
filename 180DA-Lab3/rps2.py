# client 2: subscriber

import paho.mqtt.client as mqtt
import time

count = 0

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))
    client.subscribe("ece180d/test", qos=1)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print('Unexpected Disconnect')
    else:
        print('Expected Disconnect')


def on_message(client, userdata, message):
    msg_payload = int(message.payload.decode())
    global count
    print('Received message: "' + str(msg_payload) + '" on topic "' + 
            message.topic + '" with QoS ' + str(message.qos))
    count += 1 
    print("Published Counter: ", count)

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.connect_async('mqtt.eclipseprojects.io')

client.loop_start()

while True: 
    time.sleep(1)
    pass 

# disconnect when the user presses CTRL + C
# use disconnect() to disconnect from the broker.
client.loop_stop()
client.disconnect()

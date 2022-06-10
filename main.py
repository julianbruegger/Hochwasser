# python 3.6

import random
import time
import config

from paho.mqtt import client as mqtt_client

topic = "python/mqtt"

broker = config.broker
port = config.port
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = config.username
password = config.password

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        #msg = f"messages: {msg_count}"
        msg = random.uniform(0, 100)
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        time.sleep(15)


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    


if __name__ == '__main__':
    run()
    

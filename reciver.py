#!/usr/bin/python3

# Created By Julian Bruegger
# 10.06.2022
# Questions please contact jul.bruegger(at)gmail.com
# Infos at thefloodingproject.ml


#Bibliotheken einbinden
import random
import mysql.connector
from paho.mqtt import client as mqtt_client
import time
import config

topic = "python/mqtt"

username = config.user_mqtt
password = config.password_mqtt
broker = config.broker
port = config.port
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'

mydb = mysql.connector.connect(
    host = config.host, 
    user = config.user,
    password = config.password,
    database = config.database)
mycursor = mydb.cursor()



def connect_mqtt() -> mqtt_client:
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


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        #print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        x = (msg.payload.decode())
        # print(x)
        sql(x)

    client.subscribe(topic)
    client.on_message = on_message
    

def sql(mqttdata):

    sql = "INSERT INTO wasser (time, distanz, up) VALUES (now(), %s,%s)"
    val = (mqttdata, (mqttdata))
    mycursor.execute(sql, val)
    mydb.commit()
    #print("iz working")

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
    
    


if __name__ == '__main__':
    run()

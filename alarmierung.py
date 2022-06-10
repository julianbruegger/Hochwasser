#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time
import mysql.connector
import os
import socket
from twilio.rest import Client


#Twilio Settings
account_sid = 'ACcb77a8fce7a2b54907498a6aa43f6241'
auth_token = '47aa69ecd79ad698065daeab28885181'

phone_nr = ['+41765974891']
twilio_nr= '+12173647471'
client = Client(account_sid, auth_token)


REMOTE_SERVER = "one.one.one.one"


# Define db
mydb = mysql.connector.connect(
    host="192.168.111.61", 
    user="root",
    password="123ict",
    database="bach")
mycursor = mydb.cursor()

#Overflow-Val
overflow = float('10')
#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#GPIO Pins zuweisen
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def distanz():
    # setze Trigger auf HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # setze Trigger nach 0.01ms aus LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartZeit = time.time()
    StopZeit = time.time()
 
    # speichere Startzeit
    while GPIO.input(GPIO_ECHO) == 0:
        StartZeit = time.time()
 
    # speichere Ankunftszeit
    while GPIO.input(GPIO_ECHO) == 1:
        StopZeit = time.time()
 
    # Zeit Differenz zwischen Start und Ankunft
    TimeElapsed = StopZeit - StartZeit
    # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
    # und durch 2 teilen, da hin und zurueck
    distanz = (TimeElapsed * 34300) / 2
 
    return distanz


def sql():

    sql = "INSERT INTO wasser (time, distanz, up) VALUES (now(), %s,%s)"
    val = (abstand, stand)
    mycursor.execute(sql, val)
    mydb.commit()
    #print("iz working")

def is_connected(hostname):
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(hostname)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    s.close()
    return True
  except:
     pass
  return False

if __name__ == '__main__':
    while True:
        if (is_connected(REMOTE_SERVER)) == True:
            try:
                abstand = float(distanz() - (float("6")))
                stand = (float('220'))-(abstand)
                if abstand < overflow:
                    time.sleep(120)
                    sql()
                    abstand = distanz() - (float("6"))

                    if (distanz()-10) <= abstand <= (distanz()-10):

                        if abstand < overflow:
                            sql()
                            for i in phone_nr:
                                call = client.calls.create(
                                        url='http://bach.widacher.tk/nachricht.xml',
                                        to=(i),
                                        from_=twilio_nr
                                    )
                                print ("Gemessene Entfernung = %.1f cm" % abstand)
                            for x in range(600):
                                sql()
                                time.sleep(60)
                        else:
                            sql()
                            time.sleep (60)
                    else:
                        time.sleep (60)
                #Try every 5 Mins
                else: 
                    sql()

                    time.sleep(300)
            except:
                print("error")
                GPIO.cleanup()
                os.system("sudo nohup python /home/pi/Hochwasser/alarmierung.py &")
                pass
        else:
            print("network is offline")
            time.sleep (60)

        


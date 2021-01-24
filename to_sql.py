#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time
import mysql.connector
from twilio.rest import Client

# Define db
mydb = mysql.connector.connect(
    host="***", 
    user="***",
    password="***",
    database="***")
mycursor = mydb.cursor()

#Overflow-Val
overflow = float('5')
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


if __name__ == '__main__':
    while True:
        try:
            abstand = float(distanz() - (float("6")))
            stand = (float('220'))-(abstand)
            
            sql()

            time.sleep(3)
        # Reset by pressing CTRL + C
        except:
            print("error")
            GPIO.cleanup()
            time.sleep(300)
            pass
    


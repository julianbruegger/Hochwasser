#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time
import mysql.connector
from twilio.rest import Client


#Twilio Settings
account_sid = '***'
auth_token = '***'
phone_nr = '+***'
twilio_nr='+12173647471'
client = Client(account_sid, auth_token)


# Define db
mydb = mysql.connector.connect(
    host="192.168.111.61", 
    user="root",
    password="***",
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
    val = (abstand, abstand)
    mycursor.execute(sql, val)
    mydb.commit()
    print("iz working")


if __name__ == '__main__':
    try:
        while True:
            abstand = distanz()
            if abstand < overflow:
                sql()
                call = client.calls.create(
                        url='http://bach.widacher.tk/nachricht.xml',
                        to=phone_nr,
                        from_=twilio_nr
                    )
                
                print ("Gemessene Entfernung = %.1f cm" % abstand)
        
                time.sleep(1800)

            #Try every 5 Mins
            else: 
                sql()

                time.sleep(300)
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

    

#Libraries
import RPi.GPIO as GPIO
import time
import mysql.connector
from twilio.rest import Client
import time

#Twilio Settings
account_sid = '***'
auth_token = '***'
phone_nr = '***'
twilio_nr='***'
client = Client(account_sid, auth_token)

#Alert Settings
## Distance to Owerflow the creek
owerflow = '45'


#MySQL settings
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()


def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance


def WriteSQL():
    sql = "INSERT INTO wasser (time, distanz) VALUES (now(), %s)"
    val = (distance)
    mycursor.execute(sql, val)
    mydb.commit()

if __name__ == '__main__':
    try:
        while True:
            if distance < owerflow
            call = client.calls.create(
                        url='http://connect.julian-bruegger.tk/test.xml',
                        to=phone_nr,
                        from_=twilio_nr
                    )
            #After Alert try again in 30Mins
            WriteSQL():
            time.sleep(1800)

            #Try every 5 Mins
            else: 
                WriteSQL():

                time.sleep(300)
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

    

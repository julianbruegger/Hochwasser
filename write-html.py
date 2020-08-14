import mysql.connector
import os
mydb = mysql.connector.connect(
  host="192.168.111.61",
  user="root",
  password="***",
  database="bach"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT distanz FROM wasser")

myresult = mycursor.fetchone()

distance = (myresult[0])

print (distance)

os.system (echo (distance))

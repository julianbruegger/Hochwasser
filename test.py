import socket
import mysql.connector

# Define db
mydb = mysql.connector.connect(
    host="192.168.111.61", 
    user="root",
    password="123ict",
    database="bach")
mycursor = mydb.cursor()

def sql():
    try:
      sql = "INSERT INTO wasser (time) VALUES (now())"
      val = (abstand, stand)
      mycursor.execute(sql, val)
      mydb.commit()
    #print("iz working")
    except mysql.Error as e:
            msg = 'Failure in executing query {0}. Error: {1}'.format(query, e)
            raise DatabaseError(msg) 


REMOTE_SERVER = "one.one.one.one"
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
    return None
    pass
     
  return False
if (is_connected(REMOTE_SERVER)) == True:
    print("network is online")
else:
    print("network is offline")
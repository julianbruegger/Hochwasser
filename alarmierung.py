# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import time

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
wasserstand = "30"

while True:
    if wasserstand < "40":
        
        nummer = [+41765974891]
        for i in nummer:
            account_sid = '****'
            auth_token = '+++'
            client = Client(account_sid, auth_token)
            

            if wasserstand < "100":
                #1. Alarm
                call = client.calls.create(
                                        url='http://connect.julian-bruegger.tk/test.xml',
                                        to=(i),
                                        from_='+12173647471'
                                    )

                print((i).sid)
                #2. Alarm
            elif wasserstand >"80":
                call = client.calls.create(
                                        url='http://connect.julian-bruegger.tk/test.xml',
                                        to=(i),
                                        from_='+12173647471'
                                    ) 
    else:
        time.sleep(600)

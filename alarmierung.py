
# Download the helper library from https://www.twilio.com/docs/python/install
#from twilio.rest import Client

wasserstand = '1.00'

if wasserstand < '2.00':
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        url='http://connect.julian-bruegger.tk/test.xml',
        to='+47765974891',
        from_='+15017122661'
        )
    print ('alarm')
    print(call.sid)

else:
    print ('status i.o.')
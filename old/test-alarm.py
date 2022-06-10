# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = '***'
auth_token = '***'
phone_nr = '***'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://connect.julian-bruegger.tk/alarm_martin.xml',
                        to=phone_nr,
                        from_='+12173647471'
                    )


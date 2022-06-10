from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "***"
# Your Auth Token from twilio.com/console
auth_token  = "***"

client = Client(account_sid, auth_token)



message = client.messages.create(
		to="+***", 
		from_="+***",
		body="Herzlich Wilkommen zum Hochwasser-Alarm!  -  Weitere Informationen finden sie unter http://bach.widacher.tk/  -   Zeigen sie dieses Tool auch Ihren Freunden oder Nachbarn!")

print(message.sid)

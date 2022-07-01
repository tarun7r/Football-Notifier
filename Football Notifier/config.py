from twilio.rest import Client

#twilio account info
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)


#message info
def send_message(data):
    message = client.messages.create( body= data,
                              from_='whatsapp:+xxxxxxxxxxx',
                              to='whatsapp:+xxxxxxxxxxx')








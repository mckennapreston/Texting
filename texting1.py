from twilio.rest import Client

accountSID = 'AC2c3432f82ecd5ef9188c3871dc5e49ab'

authToken = '9ced8003e209134ac2ff6ce8b8502940'

client = Client(accountSID, authToken)

TwilioNumber = '+12566678523'

mycellphone = '+17133519799'

textmessage = client.messages.create(to=mycellphone,from_=TwilioNumber, body='Hello World!')

print(textmessage.status)

# make a phone call
#call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml", to=mycellphone, from_=TwilioNumber)

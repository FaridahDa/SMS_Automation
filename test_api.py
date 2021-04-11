from twilio.rest import Client
from twilio_cred import mobile_number, twilio_token, twilio_account, twiilo_number

account_sid = twilio_account
auth_token = twilio_token
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hello Faridah",
                     from_=twiilo_number,
                     to=mobile_number
                 )

print(message.sid)


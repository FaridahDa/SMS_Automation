import random, schedule, time
from twilio.rest import Client
from twilio_cred import mobile_number, twilio_token, twilio_account, twiilo_number

MORNING_AFFIRMATIONS_TEXTS = [
    "I wake up every morning ready for a new day of exciting possibilities.",
    "Today I abandon my old habits and take up new, more positive ones.",
    "I have the power to create all the success and prosperity I desire.",
    "I am excited to wake up each morning and experience this beautiful life, that I am creating with my thoughts and visions.",
    "My life is a gift. I will use this gift with confidence, joy, and exuberance."
]

def send_sms(quotes_list=MORNING_AFFIRMATIONS_TEXTS):
    account = twilio_account
    token = twilio_token
    client = Client(account, token)
    quote = quotes_list[random.randint(0,len(quotes_list)-1)]

    client.messages.create(to=mobile_number,
                           from_=twiilo_number,
                           body=quote
                           )

#send sms in the morning
schedule.every().day.at("09:00").do(send_sms, MORNING_AFFIRMATIONS_TEXTS)

#checks whether a scheduled task is pending to be run
while True:
    schedule.run_pending()
    time.sleep(1)

from dotenv import load_dotenv
from twilio.rest import Client
import os

load_dotenv()

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

client = Client()

to_number = os.environ.get("TO_NUMBER")
from_number = os.environ.get("FROM_NUMBER")

message = client.messages.create(to=to_number, from_=from_number, body="This is a test message..")


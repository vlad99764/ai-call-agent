import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
# Set up environment variables for security
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

# Fetch current dialing permissions settings
settings = client.voice.v1.dialing_permissions.settings().fetch()

if settings.dialing_permissions_inheritance:
    updated_settings = client.voice.dialing_permissions.settings().update(
        dialing_permissions_inheritance=False
    )

    print(updated_settings.dialing_permissions_inheritance)

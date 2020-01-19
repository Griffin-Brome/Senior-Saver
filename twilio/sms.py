# Download the Python helper library from twilio.com/docs/python/install
import os
import json

from twilio.rest import Client


def send_sms():

    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)


    # Get details on user and emergency contact info

    with open('contact.json', 'r') as fin:
        contact = json.load(fin)
        emergency_contact_name = contact['emergency_contact']
        emergency_contact_phone = contact['emergency_phone']
        user_name = contact['contact_name']
        user_location = contact['contact_location']

    # Make API calls here...
        message = ("ATTENTION:" + str(emergency_contact_name) + ", " + str(user_name) 
                    + " NEEDS YOUR HELP AT LOCATION: " + str(user_location))
        client.messages.create(
            to=emergency_contact_phone,
            from_="+12053464710", # Twilio trial phone #
            body=message
        )
    return
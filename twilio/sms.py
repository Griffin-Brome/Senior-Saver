# bc hacks 2020
# Download the Python helper library from twilio.com/docs/python/install
import os
import json
from seniorSaver import seniorSaver

from twilio.rest import Client

if __name__ == "__main__":
    send_sms()

def send_sms(userId, lat, lon):

    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)


    # Get details on user and emergency contact info
    self = seniorSaver()
    db = seniorSaver.connect(self)

    contact = db['Contact']

    query = { "_id": userId }

    mydoc = contact.find(query)

    num = None

    for x in mydoc:
        num = (x['number'])

    mydoc = contact.find(query)

    for x in mydoc:
        name = (x['cName'])

    person = db['Person']

    mydoc = person.find(query)

    p_name = None

    for x in mydoc:
        p_name = (x['pName'])

    with open('contact.json', 'r') as fin:
        contact = json.load(fin)
        emergency_contact_name = contact['emergency_contact']
        user_name = contact['contact_name']

    # Make API calls here...
        message = ("ATTENTION:" + str(name) + ", " 
                    + str(p_name) 
                    + " NEEDS YOUR HELP AT LOCATION: " + str(lat) + " " + str(lon))
        client.messages.create(
            to=num,
            from_="+12053464710", # Twilio trial phone #
            body=message
        )
    return
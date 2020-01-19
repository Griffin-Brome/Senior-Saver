import os
import json

# take in a contact name and a contact phone number and save to json

def write_to_json(e_contact, e_phone, c_name, c_loc):
    contact_info = {
        "emergency_contact" : e_contact,
        "emergency_phone" : e_phone,
        "contact_name" : c_name,
        "contact_location" : c_loc
        }
    with open("contacts.json", "w+") as fout:
        json.dump(contact_info, fout)    

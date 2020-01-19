# bc hacks 2020
from flask import Flask, render_template, request
import sms
import save_to_json
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from seniorSaver import seniorSaver 
from datetime import datetime
from twilio.rest import Client


app = Flask(__name__)
self = seniorSaver()
seniorSaver.connect(self)


@app.route("/help", methods=["POST", "GET"])
def help():
    lon = request.args.get("lon")
    lat = request.args.get("lat")
    user_id = request.args.get("uid")
    sms.send_sms(user_id, lat, lon)
    print (str(lon), str(lat), str(user_id))
    seniorSaver.addIncident(self, str(datetime.now()), user_id, lon, lat, datetime.now(), 1)
    print ("DB updated")
    return "Message Sent"

@app.route("/")
def home():
    return render_template("home.html")


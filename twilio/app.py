from flask import Flask, render_template, request
import sms
import save_to_json
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

@app.route("/help")
def help():
    sms.send_sms()
    class MyForm(FlaskForm):
        name = StringField('name', validators=[DataRequired()])
    return "Message Sent"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/upload-contact", methods=["POST"]) # take in user data via POST 
def upload():
    lat = request.form.get("lat")
    lon = request.form.get("lon")
    #date = request.form.get("date")
    user_id = request.form.get("userid")
    # These are gonna be sent to the DB 
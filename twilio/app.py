from flask import Flask, render_template
import sms

app = Flask(__name__)

@app.route("/help")
def help():
    sms.send_sms()
    return "Message Sent"

@app.route("/")
def home():
    return render_template("home.html")
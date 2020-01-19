from flask import Flask
import sms

app = Flask(__name__)

@app.route("/help")
def help():
    sms.send_sms()
    return "Message Sent"
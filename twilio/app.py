from flask import Flask, render_template, request
import sms

app = Flask(__name__)

@app.route("/help", methods=["POST", "GET"])
def help():
    sms.send_sms()
    lon = request.args.get("lon")
    lat = request.args.get("lat")
    user_id = request.args.get("uid")
    print (str(lon), str(lat), str(user_id))
    return "Message Sent"

@app.route("/")
def home():
    return render_template("home.html")


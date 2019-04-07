#WhatsApp Server Aplication.
#We use Twilio as a "Man in the middle" between client and WA server. 
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/')
def hello():
    return "I'm The Server for WhatsApp ChatBot :3..."

@app.route('/sms', methods=['POST'])
def sms_reply():
    """Aquí se responde con cualquier mensaje"""
    #Fetching
    msg = request.form.get('Body')

    #Replying
    resp = MessagingResponse()
    resp.message("I'm working on development mode!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
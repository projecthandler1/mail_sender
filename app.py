from email.message import  EmailMessage
import ssl
import smtplib
import json
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
email_password='kgehtoqmddftoreb'
email_sender='project8handler@gmail.com'
app=Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'application/json'
@app.route('/')
def index():
    return 'hello'
@app.route('/mail', methods=['POST'])
def send_mail():
    record = json.loads(request.data)
    email=record['email']
    subject=record['subject']
    body=record['message']
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email
    em['Subject']=subject
    em.set_content(body)

    context=ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email,em.as_string())  
  
    return 'succces'
if __name__=="__main__":
    app.run(debug=True)
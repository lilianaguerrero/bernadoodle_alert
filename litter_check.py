import requests, smtplib
from os import environ
import time 
from bs4 import BeautifulSoup

from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import logging

mom = 'Finley'
dad = 'Otis'
available = False

def puppy_alert():
    """Send text when puppy is availble using Twilio API."""
    account_sid = environ['TWILIO_ACCOUNT_SID']
    auth_token = environ['TWILIO_AUTH_TOKEN']

    TWILIO_NUMBER = '+12058720099'


    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                            body='Puppy is availble! go to https://gailsdoodles.com/current-litters',
                            from_=TWILIO_NUMBER,
                            to='+16192895400'
                     )
    print(message.sid)

    

while True: 
    dad = environ["DAD"]
    mom = environ["MOM"]
    print(f"checking with DAD {dad} and Mom: {mom}")
    headings = []

    get_page = requests.get('https://gailsdoodles.com/current-litters')

    page_details = BeautifulSoup(get_page.text, 'html.parser')

    for headlines in page_details.find_all("h1"):
        headings.append(headlines.text.strip())

    for h1 in headings:
        if h1 == mom or h1 == dad: 
            available = True 

    if available == True:
        print("puppy found")
        # puppy_alert()
        break
    else: 
        time.sleep(3)
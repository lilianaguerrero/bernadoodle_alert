import requests
from os import environ
import time 
from bs4 import BeautifulSoup
from datetime import datetime

from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import logging


def merch_alert(phone):
    """Send text when merch is availble using Twilio API."""
    account_sid = 'AC1eba558e1072b9932b78415b79239629'
    auth_token = '060ce041d6c01e653506855f121f0f17'

    TWILIO_NUMBER = '+16466792435'

    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                            body='New Merch is available! go to https://apparel.onepeloton.com/collections/new',
                            from_=TWILIO_NUMBER,
                            to=phone
                     )
    print(message.sid)

    
def checking_merch():
    """Script that checks peloton.com for new merch"""
    updated = False

    while True: 
        # variable_link = environ.get('src')
        print(f"checking with latest timestamped URL ") #deleted before quotes: {variable_link}
        data = []
        item_data = []
        phones = ['+16197153284', '+18587404081']
        sold_out_counts = [26]
        item_counts = [50]

        get_page = requests.get('https://apparel.onepeloton.com/collections/new')

        page_details = BeautifulSoup(get_page.text, 'html.parser')

        data.append(page_details.find_all('span', class_ = 'product-list-item-badge inventory'))
        data = str(data)
        data = data.split(",")
        sold_out_count = len(data)

        item_data.append(page_details.find_all('div', class_ = 'product-list-item'))
        item_data = str(item_data)
        item_data = item_data.split(",")
        item_count = len(item_data)
        
        if sold_out_count != sold_out_counts[-1] or item_count != item_counts[-1]:
            sold_out_counts.append(sold_out_count)
            item_counts.append(item_count)
            updated = True
            print('updated = True')

        if updated == True:
            for phone in phones: 
                print("sending texts!")
                merch_alert(phone) #send text messege notification
            break
        else: 
            time.sleep(180) #sleep for 3 min 


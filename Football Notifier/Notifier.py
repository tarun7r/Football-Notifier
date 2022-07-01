from event_scraper import fetch_event
from config import send_message


import requests
import json
import time



global message_before

message_before = ""

while True:
    
    data = fetch_event()
    message = data
    if message != message_before:
        send_message(message)
        message_before = message
    
    
    time.sleep(60)
    







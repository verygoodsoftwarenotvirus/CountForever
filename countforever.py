from TwitterAPI import TwitterAPI
from num2words import num2words
import time

limit = 36
number = 1

api = TwitterAPI('CREDS', 'GO', 'RIGHT', 'HERE')

while True:
    try:
    	tweet = num2words(number).replace(" and", "") + "...ah ah ah!"
    	api.request('statuses/update', {'status': tweet})
    	number += 1
    	time.sleep(limit)
    except requests.exceptions.Timeout:
    	time.sleep(1800)  # half an hour in seconds

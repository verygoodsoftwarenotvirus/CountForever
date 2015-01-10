from TwitterAPI import TwitterAPI
from num2words import num2words
import requests
import time

limit = 36  # 100 tweets per hour
ten_minutes = 600  # in seconds
number = 1

api = TwitterAPI('CREDS', 'GO', 'RIGHT', 'HERE')

while True:
    try:
        tweet = "{}{}".format(num2words(number).replace(" and", ""), "...ah ah ah!")
        api.request('statuses/update', {'status': tweet})
        number += 1
        time.sleep(limit)
    except requests.exceptions.Timeout:
        """
        Sometimes DigitalOcean works late hours and spills coffee on its pants.
        When this happens, it needs about ten minutes to go home and change.
        """
        time.sleep(ten_minutes)

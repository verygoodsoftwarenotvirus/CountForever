from TwitterAPI import TwitterAPI
from num2words import num2words
import time

limit, number = 36, 1
phrase = "...ah ah ah!"

api = TwitterAPI('CREDS', 'GO', 'RIGHT', 'HERE')

while True:
    api.request('statuses/update',
                {'status': num2words(number).replace(" and", "") + phrase})
    number += 1
    time.sleep(limit)

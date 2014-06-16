from TwitterAPI import TwitterAPI
import time

limit = 36
number = 1

api = TwitterAPI('CREDENTIALS', 'GO', 'RIGHT', 'HERE')

while True:
    time.sleep(limit)
    api.request('statuses/update', {'status':number})
    number += 1

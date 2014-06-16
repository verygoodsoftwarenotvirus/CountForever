from TwitterAPI import TwitterAPI
import time

start = time.time()
limit = 36
number = 1

api = TwitterAPI('CREDENTIALS',
                 'GO',
                 'RIGHT',
                 'HERE')

while True:
    time.sleep(36)
    r = api.request('statuses/update', {'status':number})
    number += 1

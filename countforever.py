from TwitterAPI import TwitterAPI
import time

limit = 36
number = 1

api = TwitterAPI('API', 'STUFF', 'GOES', 'HERE')

basic = ['', 'one', 'two', 'three', 'four', 'five',
         'six', 'seven', 'eight', 'nine', 'ten',
         'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
         'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']

tens = ['', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
        'seventy', 'eighty', 'ninety']

def processNumber(num):
    hyphen = "-"
    if num % 10 == 0:
        hyphen = ''
    if num <= 20:
        tweet = (basic[num])
    elif num < 100:
        tweet = (str(tens[int(num / 10)-1]) + "-" + str(basic[num % 10]))        
    elif num < 1000:
        hundred = basic[int(num / 100)] + " hundred " 
        num = num % 100
        if num <= 20:
            hyphen = ""
            tweet = (hundred + hyphen + basic[num])
        else:
            if num % 10 == 0:
                hyphen = ""
            ten = tens[int(num/10)-1]
            tweet = (hundred + ten + hyphen + str(basic[num % 10]))
    elif num < 10000:
        thousand = basic[int(num / 1000)] + " thousand " 
        num = num % 1000
        if num < 100:
            hundred = ""
        else:
            hundred = basic[int(num / 100)] + " hundred "
        num = num % 100
        if num <= 20:
            hyphen = ""
            tweet = (thousand + hundred + str(basic[num]))
        else:
            if num % 10 == 0:
                hyphen = ""
            ten = tens[int(num/10)-1]
            tweet = (thousand + hundred + ten + hyphen + str(basic[num % 10]))
    elif num < 100000:
        orignum = num
        if int(num/1000) <= 20:
            tenthou = basic[int(num / 1000)] + " thousand "
            thousand = ""
        else:
            num = orignum / 1000
            first = tens[int(num / 10)-1]
            if int(num % 10) != 0:
                first += "-"
            second = basic[int(num % 10)]            
            tenthou = first + second + " thousand " 
        num = orignum % 1000
        if num < 100:
            hundred = ""
        else:
            hundred = basic[int(num / 100)] + " hundred "
        num = num % 100
        if num <= 20:
            hyphen = ""
            tweet = (tenthou + hundred + str(basic[num]))
        else:
            if num % 10 == 0:
                hyphen = ""
            ten = tens[int(num/10)-1]
            tweet = (tenthou + hundred + ten + hyphen + str(basic[num % 10]))
    elif num < 1000000:
        orignum = num
        num = int(num / 100000)
        hundredthou = basic[num] + " hundred "
        num = int((orignum % 100000) / 1000 / 10)
        single = int((orignum % 100000 / 1000 % 10))
        if single != 0:
            tenthou = tens[num-1] + "-" + basic[single] + " thousand "
        else:
            tenthou = tens[num-1] + " thousand "
        num = orignum % 1000
        if num < 100:
            hundred = ""
        else:
            hundred = basic[int(num / 100)] + " hundred "
        num = num % 100
        if num <= 20:
            hyphen = ""
            tweet = (hundredthou + tenthou + hundred + str(basic[num]))
        else:
            if num % 10 == 0:
                hyphen = ""
            ten = tens[int(num/10)-1]
            tweet = (hundredthou + tenthou + hundred + ten + hyphen + str(basic[num % 10]))
    return tweet

while True:
    time.sleep(limit)
    api.request('statuses/update', {'status':processNumber(number) + ', ah ah ah!'})
    number += 1

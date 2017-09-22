# -*- coding: utf-8 -*-
from __future__ import division
import sys
import datetime
import hashlib
import hmac
import random
import string
import time
import math
import json
import unirest as unirest

import logging
from decimal import Decimal

logging.basicConfig(filename='4.log',level=logging.DEBUG,format='%(asctime)s %(message)s')
key = "9c38821b478a3f04a4f720a2eb7d62c6"
secret = "526a37aeb047c5936edd53a4a1aa683e"
url= "http://api.hitbtc.com"
symbol=sys.argv[1]
quantity=sys.argv[2]
#quantityBuy=string(int(quantity*1.1))
percent=float(sys.argv[3])

print (symbol+' '+quantity)

def reqq(path,par,reqType="post"):
    nonce = str(int(time.mktime(datetime.datetime.now().timetuple()) * 1000 + datetime.datetime.now().microsecond / 1000))
    path = path +"?apikey=" + key + "&nonce=" + nonce +par
    signature = hmac.new(secret.encode(), path + par , hashlib.sha512).hexdigest()

    if reqType=="get" :
        result = unirest.get(url + path, headers={"Api-Signature": signature})
    else :
        result = unirest.post(url + path, headers={"Api-Signature": signature}, params=par)
    return result.body


def getclientorderId():
    return "".join(random.choice(string.digits + string.ascii_lowercase) for _ in range(30))

def getLastPrice(ticket):
    path= '/api/1/public/'+ticket+'/ticker'
    result = unirest.get(url + path )
    return result.body

lastPrice= Decimal(getLastPrice(symbol)['last'])
k=1+Decimal(percent)/100
buyPrice="%.6f" %  Decimal(lastPrice/k)
sellPrice="%.6f" %  Decimal(lastPrice*k)
if symbol == 'EOSUSD' :
    buyPrice="%.5f" %  Decimal(lastPrice/k)
    sellPrice="%.5f" %  Decimal(lastPrice*k)
if symbol == 'DASHUSD' :
    buyPrice="%.2f" %  Decimal(lastPrice/k)
    sellPrice="%.2f" %  Decimal(lastPrice*k)

#print  lastPrice
print  buyPrice
print  sellPrice

typeorder="limit"
#clientOrderId=getclientorderId()
logging.debug( reqq("/api/1/trading/new_order","clientOrderId=" + getclientorderId() + "&symbol="+symbol+"&side=buy&quantity="+str(quantity)+"&type="+typeorder+'&price='+str(buyPrice)))
logging.debug( reqq("/api/1/trading/new_order","clientOrderId=" + getclientorderId() + "&symbol="+symbol+"&side=sell&quantity="+str(quantity)+"&type="+typeorder+'&price='+str(sellPrice)))


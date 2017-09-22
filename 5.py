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
#from datetime import datetime
import calendar
#import requests

dt = datetime.datetime.now()

#print  dt
#print dt.timestamp()
#print  (time.mktime(dt.timetuple()))

logging.basicConfig(filename='5.log',level=logging.DEBUG,format='%(asctime)s %(message)s')
key = "9c38821b478a3f04a4f720a2eb7d62c6"
secret = "526a37aeb047c5936edd53a4a1aa683e"
url= "http://api.hitbtc.com"

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


typeorder="limit"
q=reqq("/api/1/trading/orders/active","","get")['orders']

#q=orders['orders']
i=0
while i < len(q):
    if q[i]['symbol']=='BCNUSD' :
        print q[i]
        print'clientOrderId='+q[i]['clientOrderId']
        print reqq('/api/1/trading/cancel_order','clientOrderId='+q[i]['clientOrderId'],'post')
    print q[i]['lastTimestamp']    
    z=int (q[i]['lastTimestamp']/1000)
    print datetime.datetime.fromtimestamp(z)

    i+=1
   
def getclientorderId():
    return "".join(random.choice(string.digits + string.ascii_lowercase) for _ in range(30))
quantity=1
sellPrice=0.001589

print "|"+ str(reqq("/api/1/trading/new_order","&clientOrderId=" + getclientorderId() + "&symbol=BCNUSD&side=sell&quantity="+str(quantity)+"&type=limit"+'&price='+str(sellPrice) ))

d = datetime.datetime.utcnow()
print d
unixtime = calendar.timegm(d.utctimetuple())
print unixtime


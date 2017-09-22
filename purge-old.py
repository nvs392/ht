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
#import requests
import logging
from decimal import Decimal

logging.basicConfig(filename='purge.log',level=logging.DEBUG,format='%(asctime)s %(message)s')
key = "9c38821b478a3f04a4f720a2eb7d62c6"
secret = "526a37aeb047c5936edd53a4a1aa683e"
url= "http://api.hitbtc.com"
symbol='BCNUSD'



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


deg getOrdersList(sym):
    



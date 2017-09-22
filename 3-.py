# -*- coding: utf-8 -*-
from __future__ import division
import datetime
import hashlib
import hmac
import random
import string
import time
import math
import unirest as unirest
import logging

logging.basicConfig(filename='3.log',level=logging.DEBUG,format='%(asctime)s %(message)s')

key = "9c38821b478a3f04a4f720a2eb7d62c6"
secret = "526a37aeb047c5936edd53a4a1aa683e"
url= "http://api.hitbtc.com"

coinMin={
    'XMRBTC': 0.001,
    'BTCUSD': 0.01,
    'BCNBTC': 100,
    'BCNUSD': 10,
    'XMRUSD': 0.001,
    'XMRBTC': 0.01,
    'ETHUSD': 0.001,
    'ETHBTC': 0.001,
    'LTCBTC': 0.1,
    'LTCUSD': 0.1,
    'ZECBTC': 0.001,
    'ZECUSD': 0.001,
    'BCCBTC': 0.001,
    'BCCUSD': 0.01,
    'DASHBTC': 0.001,
    'DASHUSD': 0.001

}


def reqq(path,par,reqType="post"):
    nonce = str(int(time.mktime(datetime.datetime.now().timetuple()) * 1000 + datetime.datetime.now().microsecond / 1000))
    path = path +"?apikey=" + key + "&nonce=" + nonce +par
    signature = hmac.new(secret, path + par , hashlib.sha512).hexdigest()
    if reqType=="get" :
        result = unirest.get(url + path, headers={"Api-Signature": signature})
    else :
        result = unirest.post(url + path, headers={"Api-Signature": signature}, params=par)
    return result.body

def getclientorderId():
    return "".join(random.choice(string.digits + string.ascii_lowercase) for _ in range(30))

def goTrading(symbol,side,quantity):
    clientOrderId=getclientorderId()
    typeorder="market"
    return reqq("/api/1/trading/new_order","clientOrderId=" + clientOrderId + "&symbol="+symbol+"&side="+side+"&quantity="+str(quantity)+"&type="+typeorder)

def DirectExchange (symbol,coinQuantity1,coinQuantity2):
    logging.debug( goTrading('BTCUSD','sell',1)) # продаем BTC
#   logging.debug(str(coinQuantity1) +" "+str(coinQuantity2))
    logging.debug( goTrading(symbol+'USD','buy',coinQuantity1)) # покупаем coin 
    logging.debug( goTrading(symbol+'BTC','sell',coinQuantity2)) # продаём coin

def getPrice(ticket):
    path= '/api/1/public/'+ticket+'/orderbook'
    result = unirest.get(url + path )
    return result.body
   
nonce = str(int(time.mktime(datetime.datetime.now().timetuple()) * 1000 + datetime.datetime.now().microsecond / 1000))

def check(coin) :

    qq1=getPrice('BTCUSD') # продаем BTC
    BTCUSD=qq1['bids'][2][0]             # $ за 0,01 BTC
    USD=float(BTCUSD)*0.01 # столько должно быть $
    qq2=getPrice(coin+'USD') # за $ покупаем coin 
    coinUSD=qq2['asks'][2][0]
    quantity=int(USD/float(coinUSD)/float(coinMin[coin+'USD'])) # в пунктах сколько покупать коинов
    coinCount= quantity * float(coinMin[coin+'USD'])        # количество коинов
    quantitytoUSD=int(coinCount/float(coinMin[coin+'BTC']))
    qq3=getPrice(coin+'BTC') # покупаем назад BTC
    coinBTC=qq3['bids'][2][0]
    backBTC=coinCount*float(coinBTC)
    k=backBTC/0.01
    if (float(k)>1.01) :
        logging.debug(coin+' K='+ str(k))
        DirectExchange(coin,quantity,quantitytoUSD)
    # обратный расчёт
    bcoinBTC=qq3['asks'][2][0]
    bquantity=int(float(coinMin['BTCUSD'])/float(bcoinBTC)/float(coinMin[coin+'BTC']))
    bcoin=bquantity*float(coinMin[coin+'BTC']) # коинов из 0,01 BTC
    bcoinUSD=qq2['bids'][2][0] 
    #bquantity=float(bcoin*float(bcoinUSD))
    USD=float(bcoin*float(bcoinUSD))
    BTCUSD=qq1['asks'][2][0]
    backBTC=USD/float(BTCUSD)
    k2=backBTC/0.01
    if (float(k)>1.005) :
        logging.debug(coin+'b K='+ str(k2))
    return str(k) +" "+ str(k2)

print 'BCN '+check('BCN')
print 'XMR ' +check('XMR')
print 'ETH ' +check('ETH')
print 'LTC ' +check('LTC')
print 'ZEC ' +check('ZEC')
print 'BCC ' +check('BCC')
print 'DASH ' +check('DASH')
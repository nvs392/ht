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

#logging.basicConfig(format='%(asctime)s %(message)s')
logging.basicConfig(filename='2.log',level=logging.DEBUG,format='%(asctime)s %(message)s')

key = "9c38821b478a3f04a4f720a2eb7d62c6"
secret = "526a37aeb047c5936edd53a4a1aa683e"
url= "http://api.hitbtc.com"

def getPrice(ticket,order):
    path= '/api/1/public/'+ticket+'/orderbook'
    result = unirest.get(url + path )
    return result.body[order]

nonce = str(int(time.mktime(datetime.datetime.now().timetuple()) * 1000 + datetime.datetime.now().microsecond / 1000))

#clientOrderId = "".join(random.choice(string.digits + string.ascii_lowercase) for _ in range(30))
# path = "/api/1/trading/new_order?apikey=" + key + "&nonce=" + nonce
#newOrder = "clientOrderId=" + clientOrderId + "&symbol=BTCUSD&side=buy&price=250&quantity=100&type=limit"
#signature = hmac.new(secret, path + newOrder, hashlib.sha512).hexdigest()
def checkUSDBTCBCN() :
    qq=getPrice('BTCUSD','asks')
    BTCUSD=qq[2][0]
    #print BTCUSD
    USD=0.01*float(BTCUSD) # usd for 0.01 BTC
    qq=getPrice('BCNBTC','asks')
    BCNBTC=qq[2][0]
    qq=getPrice('BCNUSD','bids')
    BCNUSD=qq[2][0]
    BCN=0.01/float(BCNBTC)
    lostBCN=BCN % 100
    BCN=(BCN//100)*100
    backUSD=BCN*float(BCNUSD)
    k=backUSD/float(USD)
 #   print BTCUSD +'  '+BCNUSD + ' ' + BCNBTC
    print str(USD)+'$->0.01->'+str(BCN)+ 'BCN->'+ str(backUSD)+'$ k='+str(k)
    return k

def checkBackBCN() :
    qq=getPrice('BCNBTC','bids')
    BCNBTC=qq[2][0]
    #print BTCUSD
    BCN=math.ceil(0.01/float(BCNBTC)/100)*100 #  BCN need for 0.01 btc
    qq=getPrice('BCNUSD','asks')
    BCNUSD=qq[2][0]

    qq=getPrice('BTCUSD','bids')
    BTCUSD=qq[2][0]
    BCN=0.01/float(BCNBTC)
    USD=BCN*float(BCNUSD)
    BCN=(BCN//100)*100
    backUSD=0.01*float(BTCUSD)
    k=backUSD/float(USD)
    #print BTCUSD +'  '+BCNUSD + ' ' + BCNBTC
    print str(USD)+"$->"+str(BCN)+ 'BCN 0.01->'+ str(backUSD)+'$!! k='+str(k)
    return k

def checkOverXMR():
    qq=getPrice('BTCUSD','asks')
    BTCUSD=qq[2][0]
    #print BTCUSD
    USD=0.01*float(BTCUSD) # usd for 0.01 BTC
    qq=getPrice('XMRBTC','asks')
    XMRBTC=qq[2][0]
    qq=getPrice('XMRUSD','bids')
    XMRUSD=qq[2][0]
    XMR=0.01/float(XMRBTC)
    #lostXMR=BCN % 100
    #BCN=(BCN//100)*100
    backUSD=XMR*float(XMRUSD)
    k=backUSD/float(USD)
  #  print BTCUSD +'  '+ XMRUSD + ' ' + XMRBTC
    print str(USD)+'$->'+str(XMR)+ 'XMR ->'+ str(backUSD)+'$ '+str(k)
    return k

def checkOverETH():
    qq=getPrice('BTCUSD','asks')
    BTCUSD=qq[2][0]
    #print BTCUSD
    USD=0.01*float(BTCUSD) # usd for 0.01 BTC
    qq=getPrice('ETHBTC','asks')
    ETHBTC=qq[2][0]
    qq=getPrice('ETHUSD','bids')
    ETHUSD=qq[2][0]
    ETH=0.01/float(ETHBTC)
    #lostXMR=BCN % 100
    #BCN=(BCN//100)*100
    backUSD=ETH*float(ETHUSD)
    k=backUSD/float(USD)
  #  print BTCUSD +'  '+ XMRUSD + ' ' + XMRBTC
    print str(USD)+'$->'+str(ETH)+ 'ETH ->'+ str(backUSD)+'$ '+str(k)
    return k

def checkOverLTC():
    qq=getPrice('BTCUSD','asks')
    BTCUSD=qq[2][0]
    #print BTCUSD
    USD=0.01*float(BTCUSD) # usd for 0.01 BTC
    qq=getPrice('LTCBTC','asks')
    LTCBTC=qq[2][0]
    qq=getPrice('LTCUSD','bids')
    LTCUSD=qq[2][0]
    LTC=0.01/float(LTCBTC)
    #lostXMR=BCN % 100
    #BCN=(BCN//100)*100
    backUSD=LTC*float(LTCUSD)
    k=backUSD/float(USD)
  #  print BTCUSD +'  '+ XMRUSD + ' ' + XMRBTC
    print str(USD)+'$->'+str(LTC)+ 'LTC ->'+ str(backUSD)+'$ '+str(k)
    return k

def checkOverEOS():
    qq=getPrice('BTCUSD','asks')
    BTCUSD=qq[2][0]
    #print BTCUSD
    USD=0.01*float(BTCUSD) # usd for 0.01 BTC
    qq=getPrice('EOSBTC','asks')
    EOSBTC=qq[2][0]
    qq=getPrice('EOSUSD','bids')
    EOSUSD=qq[2][0]
    EOS=0.01/float(EOSBTC)
    #lostXMR=BCN % 100
    #BCN=(BCN//100)*100
    backUSD=EOS*float(EOSUSD)
    k=backUSD/float(USD)
  #  print BTCUSD +'  '+ XMRUSD + ' ' + XMRBTC
    print str(USD)+'$->'+str(EOS)+ 'LTC ->'+ str(backUSD)+'$ '+str(k)
    return k

k=0;

while (float(k)<1.5) :
    k1=checkUSDBTCBCN();
   # logging.debug(k)
    if (float(k1)>1) :
        logging.debug('BCN K='+ str(k1))
    k2=checkOverXMR();
    if (float(k2)>1) :
        logging.debug('XMR K='+ str(k2))
    k3=checkOverETH()
    if (float(k3)>1) :
        logging.debug('ETH K='+ str(k3))
    k4=checkOverLTC()
    if (float(k4)>1) :
        logging.debug('LTC K='+ str(k4))
    k5=checkOverEOS()
    if (float(k5)>1) :
        logging.debug('EOS K='+ str(k5))
    k6=checkBackBCN() 
    if (float(k6)>1) :
        logging.debug('backBCN K='+ str(k6))
logging.debug(k)

#qq= result.body['BTCUSD']
#print qq['bid']
#result = unirest.post("http://api.hitbtc.com" + path, headers={"Api-Signature": signature}, params=newOrder)
#print result.body['ExecutionReport']

#path="/api/1/trading/balance?apikey=" + key + "&nonce=" + nonce
#signature = hmac.new(secret, path , hashlib.sha512).hexdigest()
#result = unirest.get(url + path, headers={"Api-Signature": signature} )
#qq=result.body['balance']

#print qq
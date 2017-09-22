import datetime
import hashlib
import hmac
import random
import string
import time
import unirest as unirest

key = "9c38821b478a3f04a4f720a2eb7d62c6"
secret = "526a37aeb047c5936edd53a4a1aa683e"
url= "http://api.hitbtc.com"
symbol='BCNBTC'
side='sell'
quantity=279
typeorder="market"


def reqq(path,par,reqType="post"):
    nonce = str(int(time.mktime(datetime.datetime.now().timetuple()) * 1000 + datetime.datetime.now().microsecond / 1000))
    path = path +"?apikey=" + key + "&nonce=" + nonce +par
    signature = hmac.new(secret, path + par , hashlib.sha512).hexdigest()
    if reqType=="get" :
        result = unirest.get(url + path, headers={"Api-Signature": signature})
    else :
        result = unirest.post(url + path, headers={"Api-Signature": signature}, params=par)
    return result.body

clientOrderId="".join(random.choice(string.digits + string.ascii_lowercase) for _ in range(30))

print clientOrderId
print reqq("/api/1/trading/new_order","clientOrderId=" + clientOrderId + "&symbol="+symbol+"&side="+side+"&quantity="+str(quantity)+"&type="+typeorder)
print reqq("/api/1/trading/order","&clientOrderId="+clientOrderId ,"get")



import datetime
import hashlib
import hmac
import random
import string
import time
import unirest as unirest

key = "da01c7e1f0dc4f166c6aa3d56add3293"
secret = "XXXXXXXXXXXXXXXXXXXXXXXXXX"
nonce = str(int(time.mktime(datetime.datetime.now().timetuple()) * 1000 + datetime.datetime.now().microsecond / 1000))

clientOrderId = "".join(random.choice(string.digits + string.ascii_lowercase) for _ in range(30))
path = "/api/1/trading/new_order?apikey=" + key + "&nonce=" + nonce
newOrder = "clientOrderId=" + clientOrderId + "&symbol=BTCUSD&side=buy&price=250&quantity=100&type=limit"
signature = hmac.new(secret, path + newOrder, hashlib.sha512).hexdigest()
result = unirest.post("http://api.hitbtc.com" + path, headers={"Api-Signature": signature}, params=newOrder)
print result.body['ExecutionReport']
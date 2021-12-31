
import requests
import time
import base64
import hmac
import hashlib
import json
import apiAccess


# tickers
api_path=  "/api/v1/public/tickers"
request = {
    'market': 'BTNT_BTC',
    'request': api_path,
    'nonce': str(int(time.time())),
}
response = apiAccess.authorise(api_path,request)
# order
api_path='/api/v1/order/new'
request={
  "market": "BTNT_BTC",
	"side" : "sell",
	"amount" : "0.1",
	"price" : "0.1",
'request': api_path,
'nonce': str(int(time.time()))
}
response_order_sell= apiAccess.authorise(api_path,request)
sell_data= response_order_sell.text
request={
  "market": "BTNT_BTC",
	"side" : "buy",
	"amount" : "0.1",
	"price" : "0.1",
'request': api_path,
'nonce': str(int(time.time()))
}
response_order_buy= apiAccess.authorise(api_path,request)
buy_data= response_order_buy.text

print(sell_data)
print(buy_data)
data= response.json()
high= data['result']
high= high['BTNT_BTC']
high= high['ticker']
high= high['high']
low= data['result']
low= low['BTNT_BTC']
low= low['ticker']
low= low['low']
price=data['result']
price=price['BTNT_BTC']
price=price['ticker']
price=price['last']
spread= int(float(high))-int(float(low))
print (spread)
# if spread>.03*price:
#
#
#
#
#  print(spread)





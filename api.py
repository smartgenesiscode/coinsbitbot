import requests
import time
import base64
import hmac
import hashlib
import json
import accesscoinsbit

# api_path = "/api/v1/account/balance"

api_path = "/api/v1/account/balances"
request = {
    'market': 'ETH_BTC',
    'request': api_path,
    'nonce': str(int(time.time())),
}


response = accesscoinsbit.api(api_path, request)


print(response.text)



'''
api_path = /api/v1/public/tickers


request: {
	market: ETH_BTC //ETH_BTC, BTC_ETH ...etc
}

## /api/v1/orders
request: {
  "market": "ETH_BTC",
	"offset": 10, //optional; default value 0
	"limit": 100 //optional; default value 50
    }



## /api/v1/account/balances
response: {
		{
    "success": true,
    "message": "",
    "result": {
            "ATB": {
                "available": "0",
                "freeze": "0"
            },
            "USD": {
                "available": "8990",
                "freeze": "0"
            },
            {...},
     }
}
}
```
'''

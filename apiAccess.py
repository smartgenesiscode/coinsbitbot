import requests
import time
import base64
import hmac
import hashlib
import json

def authorise(api_path,request):
    try:


        url = "https://coinsbit.io"
        complete_url = url + api_path
        api_key = "2ce70369fb64d2dd51107a0769e024aa"
        apisecret = "1fcaacdbc7ad7e0e291d6f8900530b2e"

        data = request
        dataJsonStr = json.dumps(data, separators=(',', ':'))
        payload = base64.b64encode(dataJsonStr.encode("ascii"))
        signature = hmac.new(apisecret.encode('ascii'), payload, hashlib.sha512).hexdigest()


        # headers for post request
        headers = {"Content-type": "application/json",
                   "X-TXC-APIKEY": api_key,
                   "X-TXC-PAYLOAD": payload,
                   "X-TXC-SIGNATURE": signature}

        return(requests.post(complete_url, headers=headers, data=dataJsonStr))


    except Exception as e:
        response = None
        print('error', e)
        return e
    # spread

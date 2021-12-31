import requests
import time
import base64
import hmac
import hashlib
import json
import config


def api(api_path, request):

    try:

        url = "https://coinsbit.io"
        complete_url = url + api_path
        api_key = config.api_key
        apisecret = config.apisecret

        data = request
        dataJsonStr = json.dumps(data, separators=(',', ':'))
        payload = base64.b64encode(dataJsonStr.encode("ascii"))
        signature = hmac.new(apisecret.encode('ascii'), payload, hashlib.sha512).hexdigest()

        # headers for post request
        headers = {"Content-type": "application/json",
                   "X-TXC-APIKEY": api_key,
                   "X-TXC-PAYLOAD": payload,
                   "X-TXC-SIGNATURE": signature}

        return requests.post(complete_url, headers=headers, data=dataJsonStr)

    except Exception as e:
        response = None
        return e




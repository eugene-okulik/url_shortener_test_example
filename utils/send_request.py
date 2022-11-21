import json

import requests


def send(method, url, body: dict = None, headers: dict = None):
    if not headers:
        headers = {
            'Content-Type': 'application/json'
        }
    else:
        headers = headers
    if body:
        body = json.dumps(body)
    return requests.request(method, url, data=body, headers=headers)

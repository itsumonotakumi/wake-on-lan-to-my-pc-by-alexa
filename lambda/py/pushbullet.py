from urllib.request import Request, urlopen
from urllib.error import URLError
from json import loads, dumps
import os


def send_message():
    _token = os.environ['ACCESS_TOKEN']
    _device_iden = os.environ['IDEN']
    _headers = {
        'Access-Token': _token,
        'Content-Type': 'application/json'
    }
    _url = 'https://api.pushbullet.com/v2/pushes'
    _data = {
        'type': 'note',
        'title': 'wol',
        'body': '',
        'device_iden': _device_iden
    }
    _json_data = dumps(_data).encode("utf-8")

    try:
        _res = Request(
            url=_url,
            method='POST',
            data=_json_data,
            headers=_headers
        )
        with urlopen(_res) as _req:
            return loads(_req.read())
    except URLError as e:
        if hasattr(e, 'reason'):
            return('We failed to reach a server. Reason: ', e.reason)
        elif hasattr(e, 'code'):
            return('The server couldn\'t fulfill the request. Code: ', e.code)

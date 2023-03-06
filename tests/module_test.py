from src.sample_01.sample import *
import requests
import json
import sys


def my_print():
    print("module_test")
    print(add_param(3))


def http_post():
    url = "http://10.10.50.156:30099/api/oauth2/oauth/token"
    head = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Authorization': 'Basic Y2xpZW50OjEyMzQ1Ng==',
        'Accept': 'application/json'
    }
    body = {
        'username': 'admin',
        'password': '123',
        'grant_type': 'password'
    }
    resp = requests.post(url=url, headers=head, params=body)
    print(resp.status_code)
    print(resp.cookies.values())
    print("content:",resp.content)
    resp_j = json.loads(resp.content)
    print(resp_j)
    print(type(resp_j))
    print(resp_j['access_token'])
    print("http_post...")


if __name__ == '__main__':
    rc = 1
    try:
        http_post()
        rc = 0
    except Exception as e:
        print('Error: %s' % e, file=sys.stderr)
    sys.exit(rc)
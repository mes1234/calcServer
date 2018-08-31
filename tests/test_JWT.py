import requests
import pytest
import jwt
import json

def test_LoginRoute():
    res= requests.post(url='http://0.0.0.0:8081/login',json={
        'username':'test',
        'password':'test',
    })
    decoded= jwt.decode(json.loads(res.content)['access_token'], 'super-secret', algorithms=['HS256'])
    assert decoded['identity']== 'test'
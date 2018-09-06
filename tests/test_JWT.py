import requests
import pytest
import jwt
import json
import os
from helpers.auth import *


@pytest.fixture(scope='session') 
def auth_preproc():
    os.environ['JWT_SECRET_KEY']="Artek"
    res= requests.post(url='http://0.0.0.0:8081/login',json={
        'username':'witek',
        'password':'1234',
    })
    token= json.loads(res.content)['access_token']
    return token

def test_FetchList(auth_preproc):
    token= auth_preproc
    header={
        'Authorization': f'Bearer {token}'
    }
    res= requests.get(url='http://0.0.0.0:8081/getList',headers=header)
    print(res)
    #TODO add real assertion error
    assert res == 1
def test_LoginRoute(auth_preproc):
    res= requests.post(url='http://0.0.0.0:8081/login',json={
        'username':'witek',
        'password':'1234',
    })
    assert decodeJWT(res,os.environ['JWT_SECRET_KEY'])['identity']== 'witek'
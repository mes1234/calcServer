import requests
import pytest
import jwt
import json
import os
from helpers.auth import *
from flask_jwt_extended import *

@pytest.fixture(scope='session') 
def auth_preproc():
    '''
    setup of test requiring token prior
    '''
    os.environ['JWT_SECRET_KEY']="Artek"
    res= requests.post(url='http://0.0.0.0:8081/login',json={
        'username':'witek',
        'password':'1234',
    })
    token= json.loads(res.content)['access_token']
    res={}
    res.update({
        'token':token
    })
    return res

def test_FetchList(auth_preproc):
    '''
    test to verify if logged in user obtains list of tools
    '''
    token= auth_preproc['token']
    header={
        'Authorization': f'Bearer {token}'
    }
    res= requests.get(url='http://0.0.0.0:8081/getList',headers=header)
    assert 'group' in res.text
def test_FetchListBroken(auth_preproc):
    '''
    test to verify if broken token is not accepted by server
    mimics test_FetchList
    '''
    token= auth_preproc['token']+'s'
    header={
        'Authorization': f'Bearer {token}'
    }
    res= requests.get(url='http://0.0.0.0:8081/getList',headers=header)
    assert 'group' not in res.text
def test_LoginRoute(auth_preproc):
    '''
    verify if loggin in works
    '''
    res= requests.post(url='http://0.0.0.0:8081/login',json={
        'username':'witek',
        'password':'1234',
    })
    assert decodeJWT(res,os.environ['JWT_SECRET_KEY'])['identity']== 'witek'
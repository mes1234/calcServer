from fnStore.generic import FnStore
import requests
import pytest
import jwt
import json
import os
from helpers.auth import *

import pytest
'''
dummy function for test
'''
def arytmetyka_add(x_lbm=1,y_kg='yello'):
    '''
    *function to calculate sum of two elements*
    '''
    res = x_+y_
    return res

def arytmetyka_diff(x_m3=1,y_m2=1):
    '''
    *function to calculate difference of two elements*
    '''
    res = x_m3-y_m2
    return res
'''
create Store object
'''
@pytest.fixture(scope='session') 
def Store():
    Store =FnStore() # create store
    Store.register(arytmetyka_add) # add dummy function
    Store.register(arytmetyka_diff) # add dummy function
    return Store
 ################################
######       TESTS       #########
 ################################ 
def test_StoreFnctListing(Store):
    '''
    Correctness of fetching list of fncts
    '''
    assert Store.listFn() == [
        {
            'id':0,
            'group':'arytmetyka',
            'name':'add'
        },
       {
            'id':1,
            'group':'arytmetyka',
            'name':'diff'
        },
    ]
def test_StoreFnctGetArgs(Store):
    '''
    Correctness of fetching list of args for fncts
    '''
    assert Store.getArgs(0) == {
        'x':{
            'value':1,
            'valueDefault':1,
            'valueType':'number',
            'valueUnit':'lbm'
        },
        'y':{
            'value':'yello',
            'valueType':'text',
            'valueDefault':'yello',
            'valueUnit':'kg'
        }
    }
def test_StoreFnctGetDesc(Store):
    '''
    Correctness of fetching description of funtion
    '''
    assert Store.getDesc(1) == "function to calculate difference of two elements"
def test_StoreFnctCalculate(Store):
    '''
    Correctness of calculating function
    '''
    id= 1
    args = Store.getArgs(id)
    dummyArgs=[1,2]
    toCalculate ={
        arg_: value_ for (arg_,value_) in zip(args.keys(),dummyArgs)
    }
    assert Store.calculate(id,toCalculate)==arytmetyka_diff(1,2)
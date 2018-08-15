from fnStore.generic import FnStore
import pytest
'''
dummy function for test
'''
def add(x=1,y=1):
    '''
    function to calculate sum of two elements
    '''
    res = x+y
    return res

def diff(x=1,y=1):
    '''
    function to calculate difference of two elements
    '''
    res = x-y
    return res
'''
create Store object
'''
@pytest.fixture(scope='session') 
def Store():
    Store =FnStore() # create store
    Store.register(add) # add dummy function
    Store.register(diff) # add dummy function
    return Store
 ################################
######       TESTS       #########
 ################################ 
def test_StoreFnctListing(Store):
    '''
    test correctness of fetching list of fncts
    '''
    assert Store.listFn() == ['add','diff']
def test_StoreFnctArgListing(Store):
    '''
    test correctness of fetching list of args for fncts
    '''
    assert Store.getArgs('add') == ['x','y']
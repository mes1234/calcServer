from fnStore.generic import FnStore
import pytest
'''
dummy function for test
'''
def arytmetyka_add(x=1,y=1):
    '''
    function to calculate sum of two elements
    '''
    res = x+y
    return res

def arytmetyka_diff(x=1,y=1):
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
    Store.register(arytmetyka_add) # add dummy function
    Store.register(arytmetyka_diff) # add dummy function
    return Store
 ################################
######       TESTS       #########
 ################################ 
def test_StoreFnctListing(Store):
    '''
    test correctness of fetching list of fncts
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


def test_StoreFnctArgListing(Store):
    '''
    test correctness of fetching list of args for fncts
    '''
    #TODO setup test to run flawlessly with VUE
    assert Store.getArgs('add') == ['x','y']
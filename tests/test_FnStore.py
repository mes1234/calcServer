from fnStore.generic import FnStore
import pytest
'''
dummy function for test
'''
def arytmetyka_add(x_lbm=1,y_kg='yello'):
    '''
    function to calculate sum of two elements
    '''
    res = x_+y_
    return res

def arytmetyka_diff(x_m3=1,y_m2=1):
    '''
    function to calculate difference of two elements
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


def test_StoreFnctGetArgs(Store):
    '''
    test correctness of fetching list of args for fncts
    '''
    assert Store.getArgs('add') == {
        'x':{
            'value':1,
            'valueType':'number',
            'valueUnit':'lbm'
        },
        'y':{
            'value':'yello',
            'valueType':'text',
            'valueUnit':'kg'
        }
    }
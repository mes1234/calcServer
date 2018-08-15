from generic import FnStore
# function store init
Store = FnStore()
def add(x=1,y=1):
    '''
    function to calculate sum of two elements
    '''
    res = x+y
    return res
###########################3
Store.register(add)
Store.listFn()

class FnStore():
    '''

    This is generic definition of class which will be used to define function

    '''
    fnStore= [] # list with functions
    def __init__(self):
        '''
        placeholder for intilization of class
        '''        
        pass
    def register(self,fnct):
        '''
        register function and add it to fnStore
        '''
        fn = {}
        fn['description']= fnct.__code__.co_consts
        fn['name']=fnct.__code__.co_name
        fn['argCount']= fnct.__code__.co_argcount
        fn['args']= fnct.__code__.co_varnames[:fnct.__code__.co_argcount]
        fn['exec']=fnct
        self.fnStore.append(fn)
    def __str__(self):
        '''
        placeholder for description of function
        '''
        pass
    def calculate(self):
        '''
        placeholder for calculation of function
        '''
        pass
    def getArgs(self,name):
        return list(list(filter(lambda x: x['name']==name,self.fnStore))[0]['args'])
    def listFn(self):
        '''
        returns list with names of all functions
        '''
        return list(map(lambda x:x['name'],self.fnStore))
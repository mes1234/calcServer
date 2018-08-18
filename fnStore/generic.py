import inspect
class FnStore():
    '''

    This is generic definition of class which will be used to define function

    '''
    fnStore= [] # list with functions
    formTypes={
        'int':'number',
        'str':'text'
    }
    def register(self,fnct):
        '''
        register function and add it to fnStore
        ''' 
        fn = {}
        args= inspect.getargspec(fnct)
        fn['description']= fnct.__code__.co_consts
        fn['group']=fnct.__code__.co_name.split("_")[0]
        fn['name']=fnct.__code__.co_name.split("_")[1]
        fn['id']=len(self.fnStore)
        fn['argCount']= fnct.__code__.co_argcount
        fn['values'] = {
            arg_: 
            {'valueUnit':unit_,
            'value':default_,
            'valueType':self.formTypes[typ_]
            } for (arg_, unit_,default_,typ_) in zip(
                list(map(lambda x: x.split("_")[0],args.args)),#extract argument name before _
                list(map(lambda x: x.split("_")[1],args.args)),#extract argument unit after _
                args.defaults, #extract default values
                list(map(lambda x:str(type(x)).split("'")[1],args.defaults)))} # extract units
        fn['exec']=fnct
        self.fnStore.append(fn)
    def calculate(self):
        '''
        placeholder for calculation of function
        '''
        pass
    def getArgs(self,name):
        '''
        fetch to user all of arguments
        '''
        return list(filter(lambda x: x['name']==name,self.fnStore))[0]['values']
    def listFn(self):
        '''
        returns list with names of all functions
        '''
        return list(map(lambda x:{'id':x['id'],'group':x['group'],'name':x['name']},self.fnStore))
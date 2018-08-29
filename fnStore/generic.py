import inspect
class FnStore():
    '''

    This is generic definition of class which will be used to define function
    #TODO add error handler to calculate
    '''
    fnStore= [] # list with functions
    formTypes={
        'float':'number',
        'int':'number',
        'str':'text',
        'list':'list'
    }
    def register(self,fnct):
        '''
        register function and add it to fnStore
        ''' 
        fn = {}
        args= inspect.getargspec(fnct)
        fn['description']= fnct.__doc__.split("*")[1] # truncate to portion of docstirng between * *
        fn['group']=fnct.__code__.co_name.split("_")[0]
        fn['name']=fnct.__code__.co_name.split("_")[1]
        fn['id']=len(self.fnStore)
        fn['argCount']= fnct.__code__.co_argcount
        fn['values'] = {
            arg_: 
            {'valueUnit':unit_,
            'value':default_,
            'valueDefault':default_,
            'valueType':self.formTypes[typ_]
            } for (arg_, unit_,default_,typ_) in zip(
                list(map(lambda x: x.split("_")[0],args.args)),#extract argument name before _
                list(map(lambda x: x.split("_")[1],args.args)),#extract argument unit after _
                args.defaults, #extract default values
                list(map(lambda x:str(type(x)).split("'")[1],args.defaults)))} # extract units
        fn['exec']=fnct
        self.fnStore.append(fn)
    def calculate(self,id,args):
        '''
        calculate function
        '''
        fnct= list(filter(lambda x: x['id']==id,self.fnStore))[0]['exec']
        return fnct(*args.values())
        pass
    def getArgs(self,id):
        '''
        fetch to user all of arguments
        '''
        return list(filter(lambda x: x['id']==id,self.fnStore))[0]['values']
    def getDesc(self,id):
        '''
        returns description of given functions by id
        '''
        return list(filter(lambda x: x['id']==id,self.fnStore))[0]['description']
    def listFn(self):
        '''
        returns list with names of all functions
        '''
        return list(map(lambda x:{'id':x['id'],'group':x['group'],'name':x['name']},self.fnStore))
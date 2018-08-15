import inspect
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
        #TODO add units 
        fn = {}
        args= inspect.getargspec(fnct)
        fn['description']= fnct.__code__.co_consts
        fn['group']=fnct.__code__.co_name.split("_")[0]
        fn['name']=fnct.__code__.co_name.split("_")[1]
        fn['id']=len(self.fnStore)
        fn['argCount']= fnct.__code__.co_argcount
        fn['args']= args.args
        fn['default']=args.defaults
        fn['types']=list(map(lambda x:str(type(x)).split("'")[1],args.defaults))
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
        '''
        TODO make return stgh like in values
                    selected: {
                        id:1,
                        group:'arytmetyka',
                        name:'dodaj'
                    },
                    values:{
                        'pierwsza': {
                            valueUnit: '%',
                            value: 1.,
                            valueType: 'number'
                        },
                        'druga': {
                            valueUnit: 'lbm',
                            value: 'Artur',
                            valueType: 'text'
                        },
                        'trzecia': {
                            valueUnit: '%',
                            value: 3.,
                            valueType: 'number'
                        },
                    }, // values to be passed to server every item has key is name, valueUnit, valueDefault, valueType
                    description: 'dodawanie trzech liczb', //string to describe tool
                    result:{}
                }
        '''
        values= {} # dict with currently
        # args= list(list(filter(lambda x: x['name']==name,self.fnStore))[0]['args'])
        # selected['id']=tool.['id']
        #  selected['group']=tool.['group']
        #   selected['name']=tool.['name']
        return list(list(filter(lambda x: x['name']==name,self.fnStore))[0]['args'])
    def listFn(self):
        '''
        returns list with names of all functions
        '''
        return list(map(lambda x:{'id':x['id'],'group':x['group'],'name':x['name']},self.fnStore))
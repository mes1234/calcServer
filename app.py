import os

from flask import Flask, request, g, jsonify
from fnStore.generic import FnStore
from fnStore.arytmetyka import *
from fnStore.geometria import *
from flask_cors import CORS




app= Flask(__name__)
CORS(app)

store=FnStore()
# TODO add method to add all of functions in module
store.register(arytmetyka_dodaj)
store.register(arytmetyka_odejmij)
store.register(arytmetyka_podziel)
store.register(arytmetyka_pomnoz)
store.register(geometria_pitagoras)
store.register(geometria_poleKola)


@app.route("/getList",methods=['GET'])
def getList():
    '''
    return list with all of available tools
    '''
    return jsonify(store.listFn())
@app.route("/getParams/<int:tool_id>",methods=['GET'])
def getParams(tool_id):
    '''
    return list with all parameters for selected tool
    '''
    return jsonify(store.getArgs(tool_id))
@app.route("/getDesc/<int:tool_id>",methods=['GET'])
def getDesc(tool_id):
    '''
    return description for selected tool
    '''
    return jsonify(store.getDesc(tool_id))
    # TODO add calculate route
if __name__ == '__main__':
    app.debug = True
    # app.config['DATABASE_NAME'] = 'library.db'
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8081))
    app.run(host=host, port=port)

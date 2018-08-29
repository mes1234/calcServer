import os

from flask import Flask, request, g, jsonify, render_template
from fnStore.generic import FnStore
from fnStore.arytmetyka import *
from fnStore.geometria import *
from fnStore.przeplyw import *
from flask_cors import CORS

class VueFlask(Flask):
  jinja_options = Flask.jinja_options.copy()
  jinja_options.update(dict(
    block_start_string='(%',
    block_end_string='%)',
    variable_start_string='((',
    variable_end_string='))',
    comment_start_string='(#',
    comment_end_string='#)',
  ))



app= VueFlask(__name__)
CORS(app)

store=FnStore()
# TODO add method to add all of functions in module
store.register(arytmetyka_dodaj)#1
store.register(arytmetyka_odejmij)#2
store.register(arytmetyka_podziel)#3
store.register(arytmetyka_pomnoz)#4
store.register(geometria_pitagoras)#5
store.register(geometria_poleKola)#6
store.register(przeplyw_kryza)#7

@app.route("/",methods=['GET'])
def serveApp():
    '''
    serve Vue app
    '''
    return render_template('index.html')
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
@app.route("/calculate",methods=['POST'])
def calculate():
    '''
    return function for given args
    '''
    dane= request.json['data']
    toolId= request.json['tool']
    return jsonify(store.calculate(toolId,dane))
if __name__ == '__main__':
    app.debug = False
    # app.config['DATABASE_NAME'] = 'library.db'
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8081))
    app.run(host=host, port=port)

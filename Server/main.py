from flask import Flask
from flask import request
import json
import trainednet



app = Flask(__name__)
@app.route('/hello')
def hello_world():
    return 'Hello, World'

@app.route('/poem', methods=['POST'])
def poem():
    poem_input = str(request.data)
    themes = trainednet.make_prediction(poem_input)
    return str(', '.join(themes))


#Calculations take request.data and run through neural net
@app.route('/calebisfat')
def FAT():
    return 'Caleb is fAT'

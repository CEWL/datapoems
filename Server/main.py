''' Caleb Lammers June 8th
This file sets up a server which takes the poem as a POST request and return a list of likely themes '''

#Import required libraries
from flask import Flask
from flask import request
import json
import trainednet

#Create route for flask app, take the poem as a request, make a prediction using the trained neural network, and return the final list of themes
app = Flask(__name__)
@app.route('/poem', methods=['POST'])
def poem():
    poem_input = str(request.data)
    themes = trainednet.make_prediction(poem_input)
    return themes

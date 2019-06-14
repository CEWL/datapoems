import numpy as np
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
import func
import config
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

global network
network = Sequential()
network.add(Dense(200, input_dim=27*config.max_characters, activation='relu'))
network.add(Dropout(0.2))
network.add(Dense(150, activation='relu'))
network.add(Dropout(0.2))
network.add(Dense(len(config.themes), activation='softmax'))

network.load_weights('weights.hdf5')
network.compile(loss='mse', optimizer='adam', metrics=['accuracy'])

global graph
graph = tf.get_default_graph()

def make_prediction(poem):

    arr = []
    text_list = []
    entry = []


    poem = func.process_poem(poem, True)
    print(poem)
    poem_binary = func.convert_poem_binary(config.max_characters, poem)

    for digit in poem_binary:
        entry.append(float(digit))

    arr.append(entry)
    arr = np.array(arr)
    with graph.as_default():
        prediction = network.predict(arr)

    themes = config.themes
    themes_scores = []

    for i in range(len(themes)):
        score = prediction[0][i]
        themes_scores.append((themes[i], round(100*score, 2)))
    themes_scores.sort(key=lambda themes_scores: themes_scores[1], reverse=True)

    output_str = "1." + str(themes_scores[0][0]) + "\n2." + str(themes_scores[1][0]) + "\n3." + str(themes_scores[2][0]) + "\n4." + str(themes_scores[3][0]) + "\n5." + str(themes_scores[4][0])
    return output_str

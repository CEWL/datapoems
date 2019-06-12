import numpy as np
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import ModelCheckpoint, TensorBoard
from sklearn.model_selection import train_test_split
import config


data = np.load('arr4.npy')

inputs = data[:, len(config.themes):]
labels = data[:, :len(config.themes)]

x_train, x_test, y_train, y_test = train_test_split(inputs, labels, test_size=0.15)

network = Sequential()
network.add(Dense(200, input_dim=27*config.max_characters, activation='relu'))
network.add(Dropout(0.2))
network.add(Dense(150, activation='relu'))
network.add(Dropout(0.2))
network.add(Dense(len(config.themes), activation='softmax'))

network.compile(loss='mse', optimizer='adam', metrics=['accuracy'])



filepath = "weights.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
tboard = TensorBoard(log_dir='./logs', write_graph=True, write_images=True)
callbacks_list = [checkpoint, tboard]

network.summary()

network.fit(x_train, y_train, epochs=20, validation_data=(x_test, y_test), callbacks=callbacks_list)

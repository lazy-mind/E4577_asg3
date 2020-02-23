"""
Model definition for CNN sentiment training


"""

import os
import tensorflow as tf
import tensorflow.keras as keras
from keras.models import Sequential
from keras.layers import Embedding, Dense, Conv1D, GlobalMaxPool1D


def keras_model_fn(_, config):
    """
    Creating a CNN model for sentiment modeling

    """
    model = Sequential()

    # https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding
    model.add(Embedding(input_length = config["padding_size"], 
                        input_dim = config["embeddings_dictionary_size"],
                        output_dim=config['embeddings_vector_size'],
                        trainable=True))

    # https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv1D
    model.add(Conv1D(100, kernel_size=2, strides=1, activation='relu'))

    # https://www.tensorflow.org/api_docs/python/tf/keras/layers/GlobalMaxPool1D
    model.add(GlobalMaxPool1D())

    # https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense
    model.add(Dense(100, activation='relu'))

    # https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense
    model.add(Dense(1, activation='sigmoid'))

    # https://www.tensorflow.org/api_docs/python/tf/keras/Model#compile    
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])    


    cnn_model = model

    return cnn_model

def save_model(model, output):
    """
    Method to save models in SaveModel format with signature to allow for serving


    """

    tf.saved_model.save(model, os.path.join(output, "1"))

    print("Model successfully saved at: {}".format(output))

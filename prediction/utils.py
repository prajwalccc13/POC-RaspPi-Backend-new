import os
import numpy as np
import tensorflow as tf
from .apps import PredictionConfig

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image

# model = tf.keras.models.load_model('xception')

labels = ['Alternaria Leaf Spot', 'Black Rot', 'Cabbage Aphid', 'Cabbage Looper', 'Healthy Leaf']
labels = ['ALF', 'BR', 'CA', 'CL', 'HL']

def predict_disease(img_path):

    '''
    Un-comment this

    image = tf.keras.preprocessing.image.load_img(img_path, target_size=(192, 192))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = image/255.0
    image = tf.expand_dims(image, 0)

    pred = PredictionConfig.model.predict(image)
    predicted_class = labels[pred.argmax(axis=-1)[0]]
    '''
    image = tf.keras.preprocessing.image.load_img(img_path, target_size=(512, 512))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = image/255.0
    image = tf.expand_dims(image, 0)

    pred = PredictionConfig.model.predict(image)
    predicted_class = labels[pred.argmax(axis=-1)[0]]

    # predicted_class = 'ALF'


    return predicted_class


# print(predict_disease('1.jpg'))
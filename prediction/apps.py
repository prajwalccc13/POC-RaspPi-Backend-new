from django.apps import AppConfig
import os
import numpy as np
import tensorflow as tf
import pathlib
from django.conf import settings


class PredictionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prediction'

    # MODEL_PATH = PATH("model")

    '''
    Uncomment This 

    # model_path = os.path.join(settings.BASE_DIR,'prediction/model/')
    # model = tf.keras.models.load_model(model_path)
    '''

    model_path = os.path.join(settings.BASE_DIR,'prediction/model/')
    model = tf.keras.models.load_model(model_path)

    def predict_disease(self, img_path):

        labels = ['Alternaria_Leaf_Spot', 'Cabbage aphid colony', 'club root', 'ring spot']

        image = tf.keras.preprocessing.image.load_img(img_path, target_size=(192, 192))
        image = tf.keras.preprocessing.image.img_to_array(image)
        image = image/255.0
        image = tf.expand_dims(image, 0)

        pred = self.model.predict(image)
        predicted_class = labels[pred.argmax(axis=-1)[0]]

        return predicted_class
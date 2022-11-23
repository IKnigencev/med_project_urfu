from keras.models import load_model
from PIL import Image
import numpy as np


img_height, img_width = 64, 64


model = load_model('./models/models_M.h5')


def get_predict_on_image(testImage: str):
    img = Image.open(testImage).resize((img_width, img_height))
    x = np.array(img, 'float64') / 255.
    x = np.array(x, 'float64') / 255.
    x = np.expand_dims(x, axis=0)

    pred = model.predict(x)
    perc = round(pred[0][1], 2) * 100

    return perc


def get_graph():
    """Основная функция отрисовки графиков"""
    return 0

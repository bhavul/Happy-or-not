from flask import Flask
from flask import render_template
from flask import request
import requests
from PIL import Image
import numpy as np
from keras.models import load_model
import os
from os import listdir
import cv2
import tensorflow as tf

app = Flask(__name__)
models_dict = {}
graph = None

# todo
# update readme.

def get_root_directory_of_this_app():
    return os.path.dirname(os.path.abspath(__file__))

def get_image_in_np_format(image_url):
    image_np = np.array(Image.open(requests.get(image_url, stream=True).raw))
    im = cv2.resize(image_np, (299, 299), interpolation=cv2.INTER_CUBIC)
    return im

def load_keras_models():
    global graph
    global models_dict
    graph = tf.get_default_graph()
    models = get_available_models()
    for modelname in models:
        model_file_path = get_root_directory_of_this_app()+"/models/"+modelname+".h5"
        model = load_model(model_file_path)
        models_dict[modelname] = model
    return models_dict


def predict_happiness(image_np, model_name):
    image = image_np.reshape((1,image_np.shape[0],image_np.shape[1],image_np.shape[2]))
    model = models_dict[model_name]
    with graph.as_default():
        prediction = model.predict(image)
    state = None
    confidence = None
    if(prediction[0][0] < 0.5):
        state = 'Happy'
        confidence = prediction[0][0]
    else:
        state = 'Not Happy'
        confidence = prediction[0][0]
    return state, confidence


def get_available_models():
    current_directory = get_root_directory_of_this_app()
    return [filename.split('.')[0] for filename in listdir(current_directory+"/models") if filename.endswith('.h5')]


@app.route('/', methods=['GET', 'POST'])
def do_prediction():
    models = get_available_models()
    if request.method == 'POST':
        model_name = request.form['modelName']
        image_url = request.form['imageUrl']
        image_np = get_image_in_np_format(image_url)
        prediction, confidence = predict_happiness(image_np, model_name)
        return render_template('index.html',models=models,show_prediction=True,imageUrl=image_url,
                               prediction=prediction, confidence=confidence)
    else:
        return render_template('index.html',models=models,show_prediction=False,)

# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
           "please wait until server has fully started"))
    load_keras_models()
    app.run(port=5000, debug=False)

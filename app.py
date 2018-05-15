from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

# todo
# fetch the requested model value from models directory and then

@app.route('/', methods=['GET', 'POST'])
def do_prediction():
    # todo - replace with model stuff
    models = ['model1','model2']
    image_url = 'http://i39.tinypic.com/anzl1k.jpg'
    prediction = 'happy!'
    confidence = '0.09'

    if request.method == 'POST':
        return render_template('index.html',models=models,show_prediction=True,imageUrl=image_url,
                               prediction=prediction, confidence=confidence)
    else:
        return render_template('index.html',models=models,show_prediction=False,)
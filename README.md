# Happy or Not?

This is an ongoing work for emotion classifier. Currently, it predicts whether people in an image are happy or not. It could be one person or multiple. 

It is based on transfer learning, utilizing Inception V3 model and last few layers have been trained over a set of images scrapped off from Instagram, for happy and non-happy (angry/sad/stressed) people. The images could contain one or more people. The model learns to about 80% validation accuracy, however is overfitting a bit right now.

As I said, it needs to be improved and incorporate more emotions. 

### How to use?

1. Install the dependencies (`pip install -r requirements.txt`)
2. Open the jupyter notebook inside experiments section, and run all the cells. On my macbook pro the training took about 45-50 minutes. So, have a coffee while it trains the first model.
3. Run the flask app (`python app.py`) and navigate to localhost:5000 in your browser. 
4. Select the model from dropdown, and try inserting an image URL which contains happy / sad person(s) and click on 'Predict'.

The page would reload in few moments and show you both your image and project's prediction for it with confidence. 

### Project Structure
The jupyter notebook inside `experiments` folder walks through each step with documentation to reach the model. 

The model(h5) file has not been attached to git because it was 200+ MB. However, all models go inside `models` directory. These are keras models that should be saved using `model.save('some_model_name.h5')`. This meanst each model should be having its weights, architecture, loss and state of optimization stored in it.
 
 The `templates` folder contains the jinja2 template which the flask app uses to showcase the html. 
 
 Lastly, `app.py` is the flask front-end to test this project out! Remember, you need to go through the notebook once to first generate a model. 
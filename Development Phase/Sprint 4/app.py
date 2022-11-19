#flask - it is used to run/serve application
from flask import Flask, render_template, request
from keras.utils import np_utils #used for one-hot encoding
from tensorflow.keras.datasets import mnist #mnist dataset
import tensorflow as tf
import pickle
import sklearn
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

app=Flask(__name__)
model = pickle.load(open("model.pkl",'rb'))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        #convert image to required format
        img=Image.open(f).convert("L")
+
-

        #resizing of input image
        img = img.resize((28, 28))
        
        #converting to image
        img2arr = np.array(img)
        
        #reshaping according to our requirement
        img2arr = img2arr.reshape(1, 28, 28, 1)

        #Predicting the Test set results
        y_pred=model.predict(img2arr)
        # print(y_pred)
        # print(np.argmax(y_pred, axis=1))
        return render_template("indexnew.html", name = np.argmax(y_pred, axis=1))

@app.route('/predict')
def predictload():
    return render_template('indexnew.html')
@app.route('/web')
def web_load():
    return render_template("result.html")

if __name__=="__main__":
    app.run(debug=True)
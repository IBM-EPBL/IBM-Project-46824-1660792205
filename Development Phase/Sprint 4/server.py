from flask import Flask, request, render_template,flash,redirect,session,abort
from models import Model
import os
import pandas as pd

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/predict', methods=["POST"])
def predict():
    age = int(request.form['age'])
    bp = int(request.form['bp'])
    sugar = int(request.form['sugar'])
    pc = int(request.form['pc'])
    pcc = int(request.form['pcc'])
    sodium = int(request.form['sodium'])
    hemo = float(request.form['hemo'])
    htn = int(request.form['htn'])
    db = int(request.form['db'])

    values = [age, bp, sugar, pc, pcc, sodium, hemo, htn,db]
    print(values)
    model = Model()
    classifier = model.randomforest_classifier()
    prediction = classifier.predict([values])
    print(f"Kidney disease = {prediction[0]}")

    return render_template("result.html", result=prediction[0])

app.secret_key = os.urandom(12)
app.run(port=5000, host='0.0.0.0', debug=True)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from flask import Flask, request, render_template
import pickle
import re
import math

app = Flask(__name__)

q = ""

@app.route("/")
def loadPage():
    return render_template("home.html", query="")

@app.route("/", methods=['POST'])
def cancerPrediction():
    
    inputQuery1 = request.form['query1']
    inputQuery2 = request.form['query2']
    inputQuery3 = request.form['query3']
    inputQuery4 = request.form['query4']
    inputQuery5 = request.form['query5']

    model = pickle.load(open('model.sav', 'rb'))

    data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5]]
    new_df = pd.DataFrame(data, columns=['texture_mean', 'perimeter_mean', 'smoothness_mean', 'compactness_mean', 'symmetry_mean'])

    single = model.predict(new_df)
    probability = model.predict_proba(new_df).max()

    if single == 1:
        diagnose = "This patient is diagnosed with Breast Cancer"
        prob = "Confident: {}".format(probability*100)
    else:
        diagnose = "This patient is not diagnosed with Breast Cancer"
        prob = "Confident: {}".format(probability*100)

    return render_template('home.html', output1=diagnose, output2=prob, query1 = request.form['query1'], query2 = request.form['query2'], query3 = request.form['query3'], query4 = request.form['query4'], query5 = request.form['query5'])

app.run()

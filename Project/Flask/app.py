from flask import Flask, render_template, request
from joblib import load
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = load("floods.save")
sc = load("transform.save")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def index():
    return render_template('index.html')

@app.route('/data_predict', methods=['POST'])
def predict():
    if request.method == 'POST':

        Temp = float(request.form['Temp'])
        Humidity = float(request.form['Humidity'])
        CloudCover = float(request.form['CloudCover'])
        ANNUAL = float(request.form['ANNUAL'])
        JanFeb = float(request.form['JanFeb'])
        MarMay = float(request.form['MarMay'])
        JunSep = float(request.form['JunSep'])
        OctDec = float(request.form['OctDec'])
        avgjune = float(request.form['avgjune'])
        sub = float(request.form['sub'])

        data = [[Temp, Humidity, CloudCover, ANNUAL,
                 JanFeb, MarMay, JunSep, OctDec,
                 avgjune, sub]]

        scaled_data = sc.transform(data)
        prediction = model.predict(scaled_data)

        if prediction[0] == 1:
            return render_template('chance.html')
        else:
            return render_template('no chance.html')

if __name__ == '__main__':
    app.run(debug=True)

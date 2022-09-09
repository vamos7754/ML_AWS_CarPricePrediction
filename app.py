
import re
from flask import Flask,jsonify,render_template,redirect,request,url_for
import numpy as np
import pandas as pd
import json
import pickle
from utils import CarPrice



app = Flask(__name__)

# *******************************Login API****************************
# @app.route('/')
# def homepage():
#     print("Flask")
#     return "HomePage"

# *****************************Postman Check***************************

# @app.route('/predict_car_prices',methods=['POST','GET'])
# def get_predicted_car_prices():
#     data = request.form

#     fueltype = data['fueltype']
#     aspiration = data['aspiration']
#     wheelbase = eval(data['wheelbase'])
#     carlength = eval(data['carlength'])
#     carwidth = eval(data['carwidth'])
#     curbweight = eval(data['curbweight'])
#     enginesize = eval(data['enginesize'])
#     boreratio = eval(data['boreratio'])
#     horsepower = eval(data['horsepower'])
#     citympg = eval(data['citympg'])
#     highwaympg = eval(data['highwaympg'])
#     carsrange = data['carsrange']
#     carbody = data['carbody']
#     enginetype = data['enginetype']

#     object_prices = CarPrice(fueltype, aspiration, wheelbase, carlength, carwidth,
#        curbweight, enginesize, boreratio, horsepower, citympg,
#        highwaympg, carsrange, carbody,enginetype)
    
#     predicted_car_prices = object_prices.get_carprice()
#     return jsonify({'Result':f"Predicted Car Price is: {predicted_car_prices}"})

# *************************************HTML Check*******************************************



@app.route('/')
def main():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():    
    if request.method == 'POST':
        fueltype = request.form['fueltype']
        # print(fueltype)
        aspiration = request.form['aspiration']
        wheelbase = request.form['wheelbase']
        carlength = request.form['carlength']
        carwidth = request.form['carwidth']
        curbweight = request.form['curbweight']
        enginesize =request.form['enginesize']
        boreratio = request.form['boreratio']
        horsepower = request.form['horsepower']
        citympg = request.form['citympg']
        highwaympg = request.form['highwaympg']
        carsrange = request.form['carsrange']
        carbody = request.form['carbody']
        enginetype = request.form['enginetype']

        object_prices = CarPrice(fueltype,aspiration,wheelbase,carlength,carwidth,curbweight,enginesize,boreratio,horsepower,citympg,
            highwaympg,carsrange,carbody,enginetype)
            
        prediction = object_prices.get_carprice() 
        
        return render_template("result.html", prediction = prediction)
   
   
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=False)

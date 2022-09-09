import pandas as pd
import numpy as np
import pickle
import json
import os
import sys
# sys.path.append(r"D:\Velocity\DataScience\Flask&ML_Deployment\ML_LR_Car_Price_Prediction_Dataset\ML_Car_Price_Prediction_Dataset")
import warnings
warnings.filterwarnings('ignore')



class CarPrice():
    def __init__(self,fueltype, aspiration, wheelbase, carlength, carwidth,
       curbweight, enginesize, boreratio, horsepower, citympg,
       highwaympg, carsrange, carbody,enginetype):
    
       self.fueltype = fueltype
       self.aspiration = aspiration
       self.wheelbase = wheelbase
       self.carlength = carlength
       self.carwidth = carwidth
       self.curbweight = curbweight
       self.enginesize = enginesize
       self.boreratio = boreratio
       self.horsepower = horsepower
       self.citympg = citympg
       self.highwaympg = highwaympg
       self.carsrange = carsrange
       self.carbody = 'carbody_' + carbody
       self.enginetype = 'enginetype_' + enginetype

    def load_model(self):
        with open("Linear_Model.pkl",'rb') as f:
            self.model = pickle.load(f)

        with open("Project_data.json",'r') as f:
            self.project_data = json.load(f)

    def get_carprice(self):
        self.load_model()
        carbody_index = self.project_data['columns'].index(self.carbody)
        enginetype_index = self.project_data['columns'].index(self.enginetype)

        test_array = np.zeros(len(self.project_data['columns']))

        test_array[0] = self.project_data['fueltype'][self.fueltype]
        test_array[1] = self.project_data['aspiration'][self.aspiration]
        test_array[2] = self.wheelbase
        test_array[3] = self.carlength
        test_array[4] = self.carwidth
        test_array[5] = self.curbweight
        test_array[6] = self.enginesize
        test_array[7] = self.boreratio
        test_array[8] = self.horsepower
        test_array[9] = self.citympg
        test_array[10] = self.highwaympg
        test_array[11] = self.project_data['carsrange'][self.carsrange]
        test_array[carbody_index] = 1
        test_array[enginetype_index] =1

        predicted_car_prices = self.model.predict([test_array])
        return predicted_car_prices

if __name__ == '__main__':

    fueltype = 'diesel'
    aspiration = 'std'
    wheelbase = 85
    carlength = 165
    carwidth = 64
    curbweight = 2600
    enginesize = 135
    boreratio = 3.1
    horsepower = 140
    citympg = 21
    highwaympg = 24
    carsrange = 'Medium'
    carbody = 'sedan'
    enginetype = 'ohc'

    object = CarPrice(fueltype, aspiration, wheelbase, carlength, carwidth,
       curbweight, enginesize, boreratio, horsepower, citympg,
       highwaympg, carsrange, carbody,enginetype)

    print(object.get_carprice())

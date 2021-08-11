# -*- coding: utf-8 -*-
"""CaloriesBurnt.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19oXoDTekKbx_sxEzjOl6l5GdkiJRB1MB

Import Dependencies
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics
from joblib import dump
from joblib import load

#Data collection and processing 
#csv --> pandas dataframe
calories = pd.read_csv('/content/calories.csv')
exersise_data = pd.read_csv('/content/exercise.csv')
calories_data = pd.concat([exersise_data, calories['Calories']], axis=1)
calories_data.replace({'Gender':{'male':0, 'female':1}}, inplace=True)

#Data analysis
calories_data.describe()

#Visualization
sns.set()

sns.countplot(calories_data['Gender'])

sns.distplot(calories_data['Age'])

sns.distplot(calories_data['Height'])

sns.distplot(calories_data['Weight'])

sns.distplot(calories_data['Calories'])

#finding correlation in dataset
correlation = calories_data.corr()

plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')

X = calories_data.drop(columns=['User_ID', 'Calories'], axis=1)
Y = calories_data['Calories']

#split data into test and training data
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=2)

#Load model
model = XGBRegressor()

#train model
model.fit(X_train, Y_train)

#Evaluate
test_data_prediction = model.predict(X_test)

mae = metrics.mean_absolute_error(Y_test, test_data_prediction)
print(mae)

input_data = (1, 20, 173, 72.5, 60, 122, 40)

id_np = pd.DataFrame([input_data], columns = ['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp'])


pred = model.predict(id_np)
print(pred)

dump(model, "cal.joblib.dat")

loaded_model = load("cal.joblib.dat")
input_data = (1, 20, 173, 72.5, 60, 122, 40)

id_np = pd.DataFrame([input_data], columns = ['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp'])

print(loaded_model.predict(id_np))
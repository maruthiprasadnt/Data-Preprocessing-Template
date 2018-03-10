# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Importing the basic and essential libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the Dataset
df = pd.read_csv('C:/Users/marut/Desktop/Masters Project/Data Engineer/Data Science/Udemy Course/Machine_Learning_AZ_Template_Folder/Data_Preprocessing/Data_Preprocessing/Data.csv')
X = df.iloc[:, :-1].values # splitting Input features and output features
y = df.iloc[:, 3].values # change the columns according to the dataset and problem requirement

# handling the missing Data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis =  0)
imputer = imputer.fit(X[:,1:3]) # Change the input columns according to the missing values inthe dataset
X[:,1:3] = imputer.transform(X[:,1:3])

# Encoding the Categorical Data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
l_x = LabelEncoder()
X[:, 0] = l_x.fit_transform(X[:, 0])  # Change the input columns according to categorical features inthe dataset
enc = OneHotEncoder(categorical_features = [0])
X = enc.fit_transform(X).toarray()
l_y = LabelEncoder()
y = l_y.fit_transform(y)

# splitting the dataset into the training set and test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
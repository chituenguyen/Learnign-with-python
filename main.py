import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('Churn_Modelling.csv')
x = dataset.iloc[:, 3:-1].values
y = dataset.iloc[:, -1].values

print(x)
print(y)
le = LabelEncoder()
# change gender
x[:, 2] = le.fit_transform(x[:, 2])
#
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])], remainder='passthrough')
x = np.array(ct.fit_transform(x))
print(x)
# split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
# feature scaling
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)
# initial ann
ann = tf.keras.models.Sequential()
# add the input and the first hidden layer
ann.add(tf.keras.layers.Dense(units=6, activation='relu'))
# add the second hidden layer
ann.add(tf.keras.layers.Dense(units=6, activation='relu'))
# add output layer
ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

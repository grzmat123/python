import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import tensorflow as tf
from tensorflow import keras

from sklearn.model_selection import train_test_split

from scipy.stats import reciprocal
from sklearn.model_selection import RandomizedSearchCV

import eli5
from eli5.sklearn import PermutationImportance

from IPython.display import display

from sklearn.preprocessing import MinMaxScaler

from numpy import mean
from numpy import std


n_neurons=47
learning_rate=1.758
input_shape=[36]
model = keras.models.Sequential()
model.add(keras.layers.InputLayer(input_shape=input_shape))
model.add(keras.layers.Dense(n_neurons, activation="sigmoid"))
model.add(keras.layers.Dense(1, activation="sigmoid"))
optimizer = keras.optimizers.SGD(lr=learning_rate)
model.compile(loss="mse", optimizer=optimizer)

df = pd.read_csv('database.csv')
print(df.head())

df = df.sample(frac=1).reset_index(drop=True)


del df['Stechiometria']
del df['Stala_sieciowa_c']



print(df.head())

target = df.pop('Stala_sieciowa_a')


X = df.values
y = target.values


print(y)
print(mean(y))

y = y.reshape(len(y), 1)
scaler = MinMaxScaler()
scaler.fit(y)
y_scale = scaler.transform(y)

scaler.fit(X)
X_scale = scaler.transform(X)

history = model.fit(X_scale, y_scale, epochs=1000)

pd.DataFrame(history.history).plot(figsize=(8,5))
plt.grid(True)
plt.show()


perm = PermutationImportance(model, random_state=1, scoring='neg_mean_absolute_error').fit(X_scale,y_scale)
display(eli5.show_weights(perm, feature_names = df.columns.tolist()))


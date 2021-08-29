# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import packages used in this project
import math
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from pandas_datareader import data as pdr
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
plt.style.use ('fivethirtyeight')


stockid = input('Please Input a FORMAL Stock ID: ')
#obtain a certain stock historical data after financial crisis
df = pdr.get_data_yahoo(stockid, start='2009-01-01')

#select 'Close' price column in df as data
data = df.filter(['Close'])
#transfer to array (numbers only)
dataset = data.values
#set training data, say, the first 80% of the sample (no decimals)
train_data_len = len(dataset)

#Scale the data to [0,1] with MiniMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))
scaled_dataset = scaler.fit_transform(dataset)

#create train data
train_data = scaled_dataset[0:train_data_len,:]
x_train = []
y_train = []

#use 30-day rolling basis to forecast future 5day prices
for i in range(30,train_data_len-5): 
    x_train.append(train_data[i-30:i,0])
    y_train.append(train_data[i:i+5,0])
#transfer x and y train data to array
x_train, y_train = np.array(x_train), np.array(y_train)
#reshape x train data
x_train=np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))


#LSTM Model
model = Sequential()
model.add(LSTM(64,return_sequences=True,input_shape=(x_train.shape[1],x_train.shape[2])))
model.add(LSTM(50,return_sequences=False))
model.add(Dense(25))
model.add(Dense(5))
model.compile(optimizer='adam', loss='mse')
#Trian!!!
model.fit(x_train, y_train, batch_size=1, epochs=1)

#ytest = model.predict(x_train)

#create test data
predict_data = scaled_dataset[len(dataset)-51:len(dataset)-1, :]

#transfer and reshape x test data
predict_data = np.array(predict_data)
predict_data = np.reshape(predict_data,(1,predict_data.shape[0],1))

#Forecast
predictions = model.predict(predict_data)
#transfer prediction to normal value
predictions = scaler.inverse_transform(predictions)
#print forecast result
print(stockid + ' Future 5 days Close Prcies '+str(predictions))

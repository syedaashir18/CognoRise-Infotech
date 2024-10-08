# -*- coding: utf-8 -*-
"""CAR_PRICE_PREDICTION.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BKmU5WwtbYF433PUpFlS418TU-ddWhfU
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('car.csv')

"""EXPLORING DATA


"""

df.shape

df.head()

df.columns

df.info()

df['CarName'].unique()

df['fueltype'].unique()

df['aspiration'].unique()

df['doornumber'].unique()

df['doornumber'].replace('two',2,inplace=True)
df['doornumber'].replace('four',4,inplace=True)
df['doornumber'].unique()

df['carbody'].unique()

df['drivewheel'].unique()

df['enginelocation'].unique()

df['wheelbase'].unique()

df['carlength'].unique()

df['carwidth'].unique()

df['carheight'].unique()

def unique(x):
    return df[x].unique()

unique('curbweight')

unique('enginetype')

unique('cylindernumber')

df['cylindernumber'].replace('four',4,inplace=True)
df['cylindernumber'].replace('six',6,inplace=True)
df['cylindernumber'].replace('five',5,inplace=True)
df['cylindernumber'].replace('three',3,inplace=True)
df['cylindernumber'].replace('twelve',12,inplace=True)
df['cylindernumber'].replace('two',2,inplace=True)
df['cylindernumber'].replace('eight',8,inplace=True)
df['cylindernumber'].unique()

unique('enginesize')

unique('fuelsystem')

unique('boreratio')

unique('stroke')

unique('compressionratio')

unique('horsepower')

unique('peakrpm')

unique('citympg')

unique('highwaympg')

unique('price')

"""DATA PREPROCESSING"""

df.info()

df.isna().sum()

df.duplicated().sum()

df.columns

df.describe()

sns.boxplot(data=df['price'])

df.columns

df.head()

df.info()

from sklearn import preprocessing
label=preprocessing.LabelEncoder()

label.fit(df.fueltype)
df.fueltype=label.transform(df.fueltype)

label.fit(df.aspiration)
df.aspiration=label.transform(df.aspiration)

label.fit(df.carbody)
df.carbody=label.transform(df.carbody)

label.fit(df.drivewheel)
df.drivewheel=label.transform(df.drivewheel)

label.fit(df.enginelocation)
df.enginelocation=label.transform(df.enginelocation)

label.fit(df.enginetype)
df.enginetype=label.transform(df.enginetype)

label.fit(df.fuelsystem)
df.fuelsystem=label.transform(df.fuelsystem)

df.head()

df.info()

df.columns

for col in df:
    sns.scatterplot(data=df, x=col, y='price')
    plt.show()

for col in df.columns:
    if df[col].dtype == 'object':
        try:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        except:
            pass

correlation_matrix = df.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

columns_to_sort=['drivewheel','wheelbase','carlength','carwidth',
                 'curbweight','cylindernumber','enginesize','fuelsystem','boreratio','horsepower','citympg','highwaympg']

independent_data_for_model=df[columns_to_sort]
independent_data_for_model.head()

x=df[['drivewheel','wheelbase','carlength','carwidth',
                 'curbweight','cylindernumber','enginesize','fuelsystem','boreratio','horsepower','citympg','highwaympg']]
y=df.price

x

y

from sklearn.linear_model import LinearRegression

linre=LinearRegression()
linre

linre.fit(x,y)

value=[[2,88.6,168.8,64.1,2548,4,130,5,3.47,111,21,27]]
predicted=linre.predict(value)
print(predicted)

linre.score(x,y)

x.head(1)

y.head(1)


# -*- coding: utf-8 -*-
"""Cinema_Tickets.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1H13t8ctp3uFYkBp2E9iuHSlN54eXnIoK
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('cinema.csv')

df.head()

df.info()

df.describe()

df.isnull()

df.isnull().sum()

df['cinema_code'].value_counts()

df['cinema_code'].unique()

df.shape

df.dtypes

df.columns

df['date'] = pd.to_datetime(df['date'])

df['date'].value_counts()

sns.heatmap(df.corr())
plt.show()

sns.lineplot(x=df['month'],y=df['total_sales'])

plt.title("Sales of Ticket Movie")
plt.xlabel("Month")
plt.ylabel("Total of Sale")

plt.show()

df['film_code'].value_counts()

df['quarter'].value_counts()

sns.barplot(x=df['film_code'],y=df['total_sales'])

plt.show()

sns.barplot(x=df['quarter'],y=df['total_sales'])
sns.lineplot(x=df['quarter'],y=df['total_sales'])

plt.title("Total Sales")
plt.xlabel("Quarter")
plt.ylabel("Total Sales")
plt.show()


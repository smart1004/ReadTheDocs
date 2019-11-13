#!/usr/bin/env python
# coding: utf-8

# # load_diabetes

# In[24]:

import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes

# In[25]:

db = load_diabetes()

# In[26]:

len(db['target'])

# In[19]:

db['data']

# In[17]:

db.feature_names

# In[20]:

# print(db.DESCR)

# In[13]:

db.data[0]

# In[27]:

# temp = pd.read_csv('https://web.stanford.edu/~hastie/Papers/LARS/diabetes.data',sep = '\t')
temp = pd.read_csv('./diabetes.csv', sep='\t')
temp.head()

# In[28]:

# SEX convet 0, 1
temp['SEX'] = temp['SEX'] - 1

# In[29]:

temp.head()

# In[30]:

x = temp.drop(['Y'], axis=1)

# In[31]:

temp.shape

# In[32]:

type(temp)

# In[33]:

y = temp[['Y']]  # DataFrame
# y = temp['Y'] #series

# In[34]:

y.head()

# In[35]:

type(y)

# In[36]:

x.shape, y.shape

# In[37]:

x.head(13)

# In[42]:

x.loc[12]

# In[38]:

x.loc[12, 'S2']

# In[39]:

print('s2 : ', x.loc[12, 'S2'])

# In[46]:

x.head()

# In[50]:

list(x)

# In[45]:

type(x)

# In[54]:

x.columns.tolist()[-6:]

# In[44]:

list(x)[-6:]

# In[57]:

min_max_cols = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6']

# In[58]:

for col in min_max_cols:
    min_x = x[col].min()
    max_x = x[col].max()
    boonmo = max_x - min_x
    x[col] = (x[col] - min_x) / boonmo

x.describe()

# In[61]:

x.head(13)

# In[62]:

print('s2 : ', x.loc[12, 'S2'])

# # Linear Regression
# 1. don't split train/valid/test

# In[63]:

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(x, y)
y_pred = lr.predict(x)

# In[66]:

type(y_pred)

# In[69]:

# last value
y_pred[-2:]

# In[20]:

print(53.44)

# # RMSE

# In[73]:

y.shape, y_pred.shape

# In[75]:

error = y - y_pred  # residual
squared_error = error ** 2
mse1 = squared_error.mean()
rmse1 = np.sqrt(mse1)
rmse1

# In[76]:

rmse1 = np.sqrt(((y - y_pred) ** 2).mean())
rmse1

# In[77]:

# In[79]:

from sklearn.metrics import mean_squared_error

rmse1 = np.sqrt(mean_squared_error(y, y_pred))
rmse1

# In[ ]:

#

# In[80]:

x.head()

# In[81]:

lr.coef_

# In[83]:

columns = x.columns.get_values()
columns

# In[41]:

df_coef = pd.DataFrame(lr.coef_, columns=columns)

# In[42]:

df_coef

# In[29]:

lr.intercept_

# #혈압BP coef

# In[32]:

x.describe()

# In[33]:

# 1.11680799e+00*(133-62)

1.11680799e+00 * 13

# # BMI

# In[43]:

df_coef

# In[44]:

lr.coef_

# In[85]:

5.60296209e+00

# S1 N Y

# In[88]:

-2.22359252e+02

# # KNN more! + data split!

# In[90]:

from sklearn.model_selection import train_test_split as split

# In[91]:

X_train, X_test, y_train, y_test = split(x, y, shuffle=True,
                                         test_size=0.33, random_state=42)

X_train.shape, X_test.shape

# In[92]:

# X_train, X_valid, y_train, y_valid = split(X_train, y_train, test_size =0.2)

# X_train.shape, y_train.shape

# In[43]:

X_train.reset_index(drop=True, inplace=True)
X_test.reset_index(drop=True, inplace=True)
y_train.reset_index(drop=True, inplace=True)
y_test.reset_index(drop=True, inplace=True)

# In[44]:

from sklearn.neighbors import KNeighborsRegressor

# In[45]:

knn = KNeighborsRegressor(n_neighbors=5, weights='distance',
                          metric='cosine')

# In[46]:

knn.fit(X_train, y_train)

# In[47]:

X_train.iloc[0]

# In[48]:

knn.kneighbors(X_test.iloc[0:1])[0]

# In[49]:

knn.kneighbors(X_test.iloc[0:1])[1][0].tolist()

# In[ ]:

# In[50]:

X_test.iloc[0:1]

# In[51]:

X_train.iloc[knn.kneighbors(X_test.iloc[0:1])[1][0].tolist()]

# In[52]:

y_test.iloc[0:1]

# In[53]:

y_train.iloc[knn.kneighbors(X_test.iloc[0:1])[1][0].tolist()]

# In[ ]:

# In[ ]:


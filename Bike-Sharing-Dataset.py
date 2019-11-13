#!/usr/bin/env python
# coding: utf-8

# In[14]:

get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ### Data Loading

# In[21]:

#data_path = 'https://raw.githubusercontent.com/RayleighKim/Example_datasets/master/Bike-Sharing-Dataset/hour.csv'
#rides = pd.read_csv(data_path)
rides = pd.read_csv('./hour.csv')

# In[22]:

rides.head()

# In[23]:

rides.drop(['casual', 'registered'], axis=1, inplace=True)
rides.head()

# In[24]:

rides[48:55]

# In[25]:

rides[48:100].plot(x='dteday',y='cnt')

# In[26]:

type(rides)

# In[27]:

rides.head()

# In[28]:

rides['ct'] = 0

rides.loc[rides['hr'].isin([7,8,9]), 'ct'] = 1
rides.loc[rides['hr'].isin([17,18,19]), 'ct'] = 2

# In[29]:

# Dummy Variable

# In[30]:

dummy_fields = ['season', 'weathersit', 'mnth', 'hr', 'weekday']
for each in dummy_fields:
    dummies = pd.get_dummies(rides[each], prefix=each, drop_first=False)
    rides = pd.concat([rides, dummies], axis=1)

# In[31]:

#### drop field
fields_to_drop = ['instant', 'dteday', 'season', 'weathersit',
                  'weekday', 'atemp', 'mnth', 'workingday', 'hr']
data = rides.drop(fields_to_drop, axis=1)
data.head()

# # Scaling
#

# In[32]:

quant_features = ['temp', 'hum', 'windspeed']
# Store scalings in a dictionary so we can convert back later
scaled_features = {}
for each in quant_features:
    mean, std = data[each].mean(), data[each].std()
    scaled_features[each] = [mean, std]
    data.loc[:, each] = (data[each] - mean)/std

# In[33]:

scaled_features

# ### Splitting the data into training, testing, and validation sets!

# In[34]:

test_data = data[-21*24:]
val_data = data[-81*24:-21*24]
train_data = data[:-81*24]

target_fields = ['cnt']
test_features, test_targets = test_data.drop(target_fields, axis=1), test_data[target_fields]
val_features, val_targets = val_data.drop(target_fields, axis=1), val_data[target_fields]
train_features, train_targets = train_data.drop(target_fields, axis=1), train_data[target_fields]

train_targets.head()

# In[35]:

# simple Linear Regression

# In[36]:

from sklearn.linear_model import LinearRegression

# In[37]:

slr = LinearRegression()

slr.fit(train_features, train_targets)

# predict
train_pred = slr.predict(train_features)
val_pred   = slr.predict(val_features)
test_pred = slr.predict(test_features)

# In[38]:

# rmse

# In[39]:

from sklearn.metrics import mean_squared_error
np.sqrt(mean_squared_error(val_targets, val_pred))

# #

# In[40]:

type(val_features)

# In[41]:

c_real = val_targets[val_features['ct']==1]
c_pred = val_pred[val_features['ct']==1]

np.sqrt(mean_squared_error(c_real, c_pred ))

# In[16]:

t_real = val_targets[val_features['ct']==2]
t_pred = val_pred[val_features['ct']==2]

np.sqrt(mean_squared_error(t_real, t_pred ))

# In[17]:

nct_real = val_targets[val_features['ct']==0]
nct_pred = val_pred[val_features['ct']==0]

np.sqrt(mean_squared_error(nct_real, nct_pred ))

# # linear regression

# In[18]:

from sklearn.linear_model import LinearRegression

# In[19]:

clr = LinearRegression()
clr.fit(train_features[train_features['ct']==1], train_targets[train_features['ct']==1])
train_pred_c, val_pred_c = clr.predict(train_features[train_features['ct']==1]), clr.predict(val_features[val_features['ct']==1])

# In[20]:

#rmse
from sklearn.metrics import mean_squared_error
np.sqrt(mean_squared_error(val_targets[val_features['ct']==1], val_pred_c))

# In[ ]:



# In[22]:

from sklearn.linear_model import LinearRegression

# In[23]:

tlr = LinearRegression()
tlr.fit(train_features[train_features['ct']==2], train_targets[train_features['ct']==2])
train_pred_t, val_pred_t = tlr.predict(train_features[train_features['ct']==2]), tlr.predict(val_features[val_features['ct']==2])

# In[24]:

from sklearn.metrics import mean_squared_error
np.sqrt(mean_squared_error(val_targets[val_features['ct']==2], val_pred_t))

# Gradient boosting

# In[26]:

from sklearn.ensemble import GradientBoostingRegressor

# In[27]:

gbr = GradientBoostingRegressor()

gbr.fit(train_features, train_targets)

train_pred_g, val_pred_g = gbr.predict(train_features), gbr.predict(val_features)

# In[28]:

from sklearn.metrics import mean_squared_error
np.sqrt(mean_squared_error(val_targets, val_pred_g))

# In[29]:

123.43389613234172-117.66746718688364

# In[ ]:




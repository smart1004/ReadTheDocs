#!/usr/bin/env python
# coding: utf-8

# In[1]:

#winequality-red.csv
import pandas as pd
import numpy as np
import tensorflow as tf

# In[2]:

#file_url =  '/content/winequality-red.csv'
file_url =  'winequality-red.csv'
wine_df = pd.read_csv(file_url, sep=';')
wine_df.head()

# In[4]:

wine_apply = wine_df.values
type(wine_apply)
#print(wine_apply[:10,:])
wine_apply[:3,:]

# In[9]:

# wine_df


# # onehot encoding : y_labe, category

# In[5]:

# onehot encoding  

print(set(wine_df["quality"]))

# In[6]:

wine_df.head()

# In[7]:

quality = wine_apply[:,-1:]

# In[8]:

quality

# In[11]:

quality_int = quality.astype(int) - 3

#범위 변환 및 int 형으로 변환 결과
print(quality_int.shape)

# In[ ]:



# In[26]:

quality_onehot = np.eye(6)[quality_int.reshape(1599)]
print(quality_onehot[:10, :])

# In[10]:

quality_onehot.shape

# # minmax normalization

# In[15]:

#minmax normalization
wine_apply_x = wine_apply[:,:-1]
#print(wine_apply_x[:10, :])

# In[17]:

wine_apply_x[:3, :]

# In[18]:

mins = wine_apply_x.min(axis = 0)
maxs = wine_apply_x.max(axis = 0)

wine_apply_x_normal = (wine_apply_x - mins)/(maxs - mins)

print(wine_apply_x_normal.shape)
print(wine_apply_x_normal[:5,:])

# # Result

# In[19]:

#X : wine_apply_x_normal
#Y : quality_onehot
train_count = int(1599 * 0.7)
test_count = 1599 - train_count
#print(train_count)

# In[21]:

# len(wine_apply_x_normal[:train_count, :])
# len(wine_apply_x_normal[train_count:, :])

# In[24]:

train_x = wine_apply_x_normal[:train_count,:]
test_x = wine_apply_x_normal[train_count:,:] # from train_count

# In[27]:

train_y = quality_onehot[:train_count,:]
test_y = quality_onehot[train_count:,:]

print(train_x.shape, train_y.shape)
print(test_x.shape, test_y.shape)

print(train_x[:5,:])
print(train_y[:5,:])
print(test_x[:5,:])
print(test_y[:5,:])

# # train_x

# In[28]:

print(train_x.shape)
print(train_x[:5,:])

# # test_x

# In[29]:

print(test_x.shape)
print(test_x[:5,:])

# # train_y

# In[30]:

print(train_y.shape)
print(train_y[:5,:])

# # test_y

# In[31]:

print(test_y.shape)
print(test_y[:5,:])

# In[ ]:



# In[ ]:




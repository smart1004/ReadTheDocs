#!/usr/bin/env python
# coding: utf-8

# ### Problem 03 : 문제
# ### Keras 합성곱 인공신경망 (CNN)을 활용한 손글씨 인식
# ####  ===> 올바른 결과가 출력될 수 있도록 주석처리 된 (1) ~ (5) 번을 채워 넣으시오.

# #### 필요한 패키지를 불러온다

# In[1]:

# 다음은 한번만.
#!pip install keras

# In[2]:

import os
os.environ['CUDA_VISIBLE_DEVICES'] = "0"
from keras import backend as K

# In[3]:

import pandas as pd
import numpy as np
import warnings
import keras
from sklearn.model_selection import train_test_split
from keras.utils.data_utils import get_file

?keras
# ?keras.datasets.mnist
# In[4]:

from keras.datasets.mnist import load_data

# In[5]:

from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# In[6]:

from keras.utils import to_categorical
from keras.optimizers import Adam #, RMSprop, SGD
import matplotlib.pyplot as plt

# In[7]:

# ?keras.models

# In[8]:

# !ls c:\programdata\venv36_3\lib\site-packages\keras\engine\sequential.py

# In[9]:

get_ipython().run_line_magic('matplotlib', 'inline')
warnings.simplefilter('ignore')

# In[ ]:



# #### 데이터를 불러와서 준비한다

# In[10]:

from myutil import load_data
#(X_train, y_train), (X_test, y_test)= mnist.load_data()
(X_train, y_train), (X_test, y_test) = load_data()
X_train = X_train/255.                      # 정규화.
X_test = X_test/255.                        # 정규화.

# In[11]:

print("-"*50)
print("Training data X shape: {}".format(X_train.shape))
print("Training data y shape: {}".format(y_train.shape))
print("-"*50)
print("Test data X shape: {}".format(X_test.shape))
print("Test data y shape: {}".format(y_test.shape))
print("-"*50)

# #### 시각화 해본다.

# In[12]:

n_image = 0                                       # 이미지 번호.
plt.imshow(X_train[n_image,:,:],cmap="Greys")
plt.show()

# In[13]:

X_train.shape

# #### 차원변환

# In[14]:

X_train = np.expand_dims(X_train, -1)  #X_train = X_train.reshape(-1,28,28,1) # 채널 추가
X_test = X_test.reshape(-1,28,28,1)
X_train.shape

# In[15]:

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)
#n_vars = X_train.shape[1]
y_train.shape

# In[ ]:



# #### 모형정의

# In[16]:

# 합성곱 신경망.
#hold_prob = 0.25
my_model = Sequential()
my_model.add(Conv2D(filters=32, kernel_size=(3,3), padding='same', strides=(1,1), activation="relu", input_shape=(28,28,1)))
#my_model.add(MaxPooling2D(pool_size=(2,2)))
my_model.add(Conv2D(filters=64, kernel_size=(3,3), padding='same', strides=(1,1), activation="relu"))
my_model.add(MaxPooling2D(pool_size=(2,2)))

# In[17]:

# my_model.add  <드롭아웃 layer를 추가한다. rate=hold_prob 적용 (2)>
my_model.add(Dropout(rate=0.25))
my_model.add(Flatten())

# ### 아래가 문제

# In[18]:

# https://tykimos.github.io/DeepBrick/

# In[19]:

# my_model.add  <fully connected layer를 추가한다. (1)>
my_model.add(Dense(128, activation="relu"))    #, input_dim=1024

# In[20]:

my_model.add(Dropout(rate=0.5))

"""Dropout이 어디에 위치하니? 이걸 알아야 적을수 있을 걸 """
# In[21]:

my_model.add(Dense(units = 10, activation="softmax"))

# In[22]:

# 모형의 구조를 본다.
my_model.summary()

# #### 최적화 방법과 손실함수를 정의하며 학습모형을 컴파일한다.

# In[23]:

n_epochs = 20 #5
n_batch_size = 200
learn_rate = 0.01

# In[24]:

# optimizer=       < 최적화 방법을 정의한다. (3)>
# my_model.compile    <컴파일 방법을 compile의 인자값으로 정의한다. (4)>
#optimizer = Adam(lr=0.01)
my_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy']) #optimizer='sgd'

# In[25]:

# ?keras.metrics.categorical_accuracy()

# #### 학습 실행. 손실함수의 변화를 시각화 한다.

# In[26]:

my_summary = my_model.fit(X_train, y_train, epochs=n_epochs, batch_size = n_batch_size,
                          validation_split = 0.2, verbose = 1)

my_summary.history
# In[28]:

# plt.plot(my_summary.history['categorical_accuracy'], c="g")
plt.plot(my_summary.history['acc'], c="g")
plt.plot(my_summary.history['val_acc'], c="r")
plt.title('Training History')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='lower right')
plt.show()

# #### 예측 및 결과 평가 (test Accuracy 계산)

# In[29]:

# ACC =  <정확도 계산 방법을 코딩하시오 (5)>. HINT: evaluate() 사용.
# np.round(ACC,3)
_, ACC = my_model.evaluate(X_test, y_test, batch_size=32)
print('## evaluation loss and_metrics ##')
np.round(ACC,3)

# In[30]:

del my_model
K.clear_session()

# In[ ]:



# In[ ]:




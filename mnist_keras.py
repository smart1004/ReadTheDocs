#!/usr/bin/env python
# coding: utf-8
import os

os.environ['CUDA_VISIBLE_DEVICES'] = "0"

#-----------------------------------------------------------------------------------------------------------------------
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense

# MNIST data
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print(train_images.shape, train_labels.shape, test_images.shape, test_labels.shape);
print("")

train_images = train_images.reshape(train_images.shape[0], 784).astype('float32') / 255.0
test_images = test_images.reshape(test_images.shape[0], 784).astype('float32') / 255.0
train_labels = np_utils.to_categorical(train_labels)  # One-Hot Encoding
test_labels = np_utils.to_categorical(test_labels)  # One-Hot Encoding

# Model
model = Sequential()
model.add(Dense(256, activation='relu'))  # units=256, activation='relu'
model.add(Dense(256, activation='relu'))  # units=256, activation='relu'
model.add(Dense(256, activation='relu'))  # units=256, activation='relu'
model.add(Dense(10, activation='softmax'))  # units=10, activation='softmax'
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# Training
model.fit(train_images, train_labels, epochs=10, batch_size=128, verbose=1)
# Testing
_, accuracy = model.evaluate(test_images, test_labels)
print('Accuracy: ', accuracy)  # Accuracy:  0.9488
model.summary()

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense

# MNIST data
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print(train_images.shape, train_labels.shape, test_images.shape, test_labels.shape)
train_images = train_images.reshape(train_images.shape[0], 784).astype('float32') / 255.0
test_images = test_images.reshape(test_images.shape[0], 784).astype('float32') / 255.0
train_labels = np_utils.to_categorical(train_labels)  # One-Hot Encoding
test_labels = np_utils.to_categorical(test_labels)  # One-Hot Encoding
# Model
model = Sequential()
model.add(Dense(10, activation='softmax'))  # units=10, activation='softmax'
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
# Training
model.fit(train_images, train_labels, epochs=10, batch_size=128, verbose=1)
# Testing
_, accuracy = model.evaluate(test_images, test_labels)
print('Accuracy: ', accuracy)  # Accuracy:  0.8995
model.summary()

# In[ ]:


# In[ ]:

import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Data
x_data = np.array([[1, 2], [2, 3], [3, 1], [4, 3], [5, 3], [6, 2]])
y_data = np.array([[0], [0], [0], [1], [1], [1]])
# Model, Cost, Train
model = Sequential()
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))

model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])
model.fit(x_data, y_data, epochs=10000, verbose=1)
model.summary()
# Inference
print('get_weights()', model.get_weights());
print('')
print(model.predict(x_data))


#-----------------------------------------------------------------------------------------------------------------------
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Conv2D, pooling, Flatten, Dense

# In[4]:

# MNIST data
# (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
from myutil import load_data

(train_images, train_labels), (test_images, test_labels) = load_data()

# In[5]:

print(train_images.shape, train_labels.shape, test_images.shape, test_labels.shape);
print('\n')
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1).astype('float32') / 255.0
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1).astype('float32') / 255.0
train_labels = np_utils.to_categorical(train_labels)  # One-Hot Encoding
test_labels = np_utils.to_categorical(test_labels)  # One-Hot Encoding
# Model
model = Sequential()
model.add(Conv2D(32, (3, 3), padding='same', strides=(1, 1), activation='relu', input_shape=(28, 28, 1)))
print(model.output_shape)
model.add(pooling.MaxPooling2D(pool_size=(2, 2)))
print(model.output_shape)
model.add(Conv2D(64, (3, 3), padding='same', strides=(1, 1), activation='relu'))
print(model.output_shape)
model.add(pooling.MaxPooling2D(pool_size=(2, 2)))
print(model.output_shape)
model.add(Flatten())

model.add(Dense(5000, activation='relu'))

model.add(Dense(10, activation='softmax'))  # units=10, activation='softmax'
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
# Training
epochs = 3  # 5
model.fit(train_images, train_labels, epochs=5, batch_size=32, verbose=1)
# Testing
_, accuracy = model.evaluate(test_images, test_labels)
print('Accuracy: ', accuracy)
model.summary()



#-----------------------------------------------------------------------------------------------------------------------

from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Conv2D, pooling, Flatten, Dense
# MNIST data
# (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
from myutil import load_data

(train_images, train_labels), (test_images, test_labels) = load_data()

print(train_images.shape, train_labels.shape, test_images.shape, test_labels.shape)
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1).astype('float32') / 255.0
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1).astype('float32') / 255.0
train_labels = np_utils.to_categorical(train_labels)  # One-Hot Encoding
test_labels = np_utils.to_categorical(test_labels)  # One-Hot Encoding
# Model
model = Sequential()
model.add(Conv2D(32, (3, 3), padding='same', strides=(1, 1), activation='relu', input_shape=(28, 28, 1)))
# print(model.output_shape)
model.add(Conv2D(64, (3, 3), padding='same', strides=(1, 1), activation='relu'))
# print(model.output_shape)

model.add(Flatten())
model.add(Dense(10, activation='softmax'))  # units=10, activation='softmax'
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
# Training
model.fit(train_images, train_labels, epochs=5, batch_size=32, verbose=1)
# Testing
_, accuracy = model.evaluate(test_images, test_labels)
print('Accuracy: ', accuracy)
model.summary()




#-----------------------------------------------------------------------------------------------------------------------
# Conv2D
#-----------------------------------------------------------------------------------------------------------------------

from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Conv2D, pooling, Flatten, Dense
# MNIST data
# (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
from myutil import load_data

(train_images, train_labels), (test_images, test_labels) = load_data()

print(train_images.shape, train_labels.shape, test_images.shape, test_labels.shape)
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1).astype('float32') / 255.0
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1).astype('float32') / 255.0
train_labels = np_utils.to_categorical(train_labels)  # One-Hot Encoding
test_labels = np_utils.to_categorical(test_labels)  # One-Hot Encoding
# Model
model = Sequential()
model.add(Conv2D(32, (3, 3), padding='same', strides=(1, 1), activation='relu', input_shape=(28, 28, 1)))
# print(model.output_shape)
model.add(pooling.MaxPooling2D(pool_size=(2, 2)))
# print(model.output_shape)
model.add(Conv2D(64, (3, 3), padding='same', strides=(1, 1), activation='relu'))
# print(model.output_shape)
model.add(pooling.MaxPooling2D(pool_size=(2, 2)))
# print(model.output_shape)
model.add(Flatten())
model.add(Dense(10, activation='softmax'))  # units=10, activation='softmax'
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
# Training
model.fit(train_images, train_labels, epochs=20, batch_size=128, verbose=1)
# Testing
_, accuracy = model.evaluate(test_images, test_labels)
print('Accuracy: ', accuracy)
model.summary()

# In[ ]:




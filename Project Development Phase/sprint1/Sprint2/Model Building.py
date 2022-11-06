# -*- coding: utf-8 -*-
"""HWDR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wiuPGWsBXpNpiOhUHPHmduuAoZ8zTzAx
"""

!pip install matplotlib

!apt-get -qq install -y libfluidsynth1

# https://pypi.python.org/pypi/libarchive
!apt-get -qq install -y libarchive-dev && pip install -U libarchive
import libarchive

!apt-get -qq install -y graphviz && pip install pydot
import pydot

!pip install cartopy
import cartopy

"""# Importing The Required Libraries"""

import numpy as np
import tensorflow
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.layers import Conv2D
from keras.optimizers import Adam
from keras.utils import np_utils
import matplotlib.pyplot as plt

"""# **Load** **Data**"""

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train.shape)
print(x_test.shape)

"""# **Analyzing The** **Data**"""

x_train[0]

plt.imshow(x_train[50000])     #ploting the index=image

np.argmax(y_train[5000])

"""# **Reshaping Datase**t """

x_train = x_train.reshape(60000, 28, 28, 1).astype('float32')
x_test = x_test.reshape(10000, 28, 28, 1).astype('float32')

"""## **Applying** **One** **Hot** **Encoding**"""

number_of_classes = 10
y_train = np_utils.to_categorical(y_train, number_of_classes)
y_test = np_utils.to_categorical(y_test, number_of_classes)

"""# **Model** **Building**"""

model = Sequential()

"""# **Add** **CNN** **Layers**"""

model.add(Conv2D(64, (3,3), input_shape=(28, 28, 1), activation='relu'))
model.add(Conv2D(32, (3,3), activation='relu'))
model.add(Flatten())
model.add(Dense(number_of_classes, activation ='softmax'))

"""# **Compiling** **the** **Model**"""

model.compile(loss='categorical_crossentropy', optimizer="Adam", metrics=['accuracy'])

"""# **Train** **the** **Model**"""

from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau

model.fit(x_train,y_train,validation_data=(x_test,y_test),epochs=5,batch_size=32)

"""# **OBSERVING** **THE** **METRICS**"""

metrics=model.evaluate(x_test,y_test,verbose=0)

print("Mertics(Test loss & Test Accuracy):")
print(metrics)

"""# **Test** **the** **Model**"""

from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau

from keras.models import load_model
import matplotlib.pyplot as plt

"""# **Saving** **the** **Model**"""

model.save('models/mnistCNN.h5')

"""# **create** **the** **model**"""

model=Sequential()

model.add(Conv2D(64,(3,3),input_shape=(28,28,1),activation="relu"))

model.add(Conv2D(32,(3,3),activation='relu'))

model.add(Flatten())

model.add(Dense(number_of_classes,activation="softmax"))

"""# **Train** **The** **Model**(**fitting** **the** **model**)"""

from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau

img=Image.open('img_1.png')
plt.imshow(img)

Epoch 1/5
1875/1875 [==============================] - 169s 89ms/step - loss: 0.2433 - accuracy: 0.9507 - val_loss: 0.0844 - val_accuracy: 0.9752
Epoch 2/5
1875/1875 [==============================] - 178s 95ms/step - loss: 0.0711 - accuracy: 0.9784 - val_loss: 0.0694 - val_accuracy: 0.9780
Epoch 3/5
1875/1875 [==============================] - 172s 92ms/step - loss: 0.0472 - accuracy: 0.9849 - val_loss: 0.0947 - val_accuracy: 0.9717
Epoch 4/5
1875/1875 [==============================] - 148s 79ms/step - loss: 0.0357 - accuracy: 0.9889 - val_loss: 0.0946 - val_accuracy: 0.9767
Epoch 5/5
1875/1875 [==============================] - 137s 73ms/step - loss: 0.0265 - accuracy: 0.9916 - val_loss: 0.0907 - val_accuracy: 0.9793
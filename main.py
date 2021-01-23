import tensorflow as tf
from tensorflow.keras.layers import *
import pickle
from keras.utils import to_categorical
import numpy as np
from sklearn.model_selection import train_test_split

model = tf.keras.Sequential([
    # 입력받는 사진의 크기가 150 * 150 px 이고 RGB 색상이므로 input_shape는 (150, 150, 3) 가 된다.
    Conv2D(32, (3, 3), input_shape=(150, 150, 3), activation="relu"),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(32, (3, 3), activation="relu"),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(64, (3, 3), activation="relu"),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(64, (3, 3), activation="relu"),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(64, (3, 3), activation="relu"),
    MaxPooling2D(pool_size=(2, 2)),
    MaxPooling2D(pool_size=(2, 2)),

    Flatten(),
    Dense(256, activation="relu"),
    Dropout(0.25), # 뉴런의 1/4 를 사용하지 않음으로써 과적합을 막음.
    Dense(2, activation="sigmoid")
])

model.summary()

X = []
y = []
with open("dataset/pkl/dataset2d_X.pkl", "rb") as data:
    temp = pickle.load(data)
    X += temp
    y += [0 for i in range(len(temp))]

with open("dataset/pkl/dataset3d_X.pkl", "rb") as data:
    temp = pickle.load(data)
    X += temp
    y += [1 for i in range(len(temp))]

y = to_categorical(y)

X_train, X_test, y_train, y_test = train_test_split(np.array(X), np.array(y), test_size=0.33, random_state=321)

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=50, batch_size=30)
result = model.predict(X_test)
loss, acc = model.evaluate(X_test, y_test, verbose=2)

model.save("model/model")  # 로드할 때는 tf.keras.models.load_model('model/model')

from keras.preprocessing.image import img_to_array
import os
from tqdm import tqdm
from PIL import Image
import pickle

dataset2d_X = []
for filename in tqdm(os.listdir("dataset/2d/")):
    try:
        dataset2d_X.append(img_to_array(Image.open(
            "dataset/2d/" + filename).resize((150, 150)).convert("RGB")))
    except:
        pass

with open("dataset/pkl/dataset2d_X.pkl", "wb") as file:
    pickle.dump(dataset2d_X, file)

dataset3d_X = []
for filename in tqdm(os.listdir("dataset/3d/")):
    try:
        dataset3d_X.append(img_to_array(Image.open(
            "dataset/3d/" + filename).resize((150, 150)).convert("RGB")))
    except:
        pass

with open("dataset/pkl/dataset3d_X.pkl", "wb") as file:
    pickle.dump(dataset3d_X, file)
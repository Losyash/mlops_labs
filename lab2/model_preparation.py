import os
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
from settings import (
    DATASET_PREFIX, DATASET_PATH, DATASET_TRAIN_FOLDER,
    DATASET_PROCESSED_FOLDER, MODEL_PATH
)

if not os.path.exists(f'{DATASET_PREFIX}/{MODEL_PATH}'):
    os.makedirs(f'{DATASET_PREFIX}/{MODEL_PATH}')

X_train = pd.read_csv(f'{DATASET_PREFIX}/{DATASET_PATH}/{DATASET_PROCESSED_FOLDER}/{DATASET_TRAIN_FOLDER}/X_train_data.csv')
Y_train = pd.read_csv(f'{DATASET_PREFIX}/{DATASET_PATH}/{DATASET_PROCESSED_FOLDER}/{DATASET_TRAIN_FOLDER}/Y_train_data.csv')

model = LinearRegression()
model.fit(X_train, Y_train)

with open(f'{DATASET_PREFIX}/{MODEL_PATH}/model.pickle', 'wb') as f:
    pickle.dump(model, f)
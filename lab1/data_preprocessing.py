import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from settings import (
    DATASET_PATH, DATASET_TRAIN_FOLDER, DATASET_TEST_FOLDER,
    DATASET_RAW_FOLDER, DATASET_PROCESSED_FOLDER
)


if not os.path.exists(f'{DATASET_PATH}/{DATASET_PROCESSED_FOLDER}'):
    os.makedirs(f'{DATASET_PATH}/{DATASET_PROCESSED_FOLDER}')

if not os.path.exists(f'{DATASET_PATH}/{DATASET_PROCESSED_FOLDER}/{DATASET_TRAIN_FOLDER}'):
    os.makedirs(f'{DATASET_PATH}/{DATASET_PROCESSED_FOLDER}/{DATASET_TRAIN_FOLDER}')

if not os.path.exists(f'{DATASET_PATH}/{DATASET_PROCESSED_FOLDER}/{DATASET_TEST_FOLDER}'):
    os.makedirs(f'{DATASET_PATH}/{DATASET_PROCESSED_FOLDER}/{DATASET_TEST_FOLDER}')


train_data = pd.read_csv(f'{DATASET_PATH}/{DATASET_RAW_FOLDER}/{DATASET_TRAIN_FOLDER}/train_data.csv')
test_data = pd.read_csv(f'{DATASET_PATH}/{DATASET_RAW_FOLDER}/{DATASET_TEST_FOLDER}/test_data.csv')

# Обработка тренировочных данных
X_train = train_data.drop('day_temp', axis=1)
y_train = train_data['day_temp']

data_scaler = StandardScaler()

X_train = data_scaler.fit_transform(X_train)

pd.DataFrame(X_train).to_csv(f'{DATASET_PATH}/{DATASET_PROCESSED_FOLDER}/{DATASET_TRAIN_FOLDER}/X_train_data.csv', index=False)
pd.DataFrame(y_train).to_csv(f'{DATASET_PATH}/{DATASET_PROCESSED_FOLDER}/{DATASET_TRAIN_FOLDER}/Y_train_data.csv', index=False)

# Обработка тестовых данных
X_test = test_data.drop('day_temp', axis=1)
y_test = test_data['day_temp']

X_test = data_scaler.transform(X_test)

pd.DataFrame(X_test).to_csv(f'{DATASET_PATH}/{DATASET_PROCESSED_FOLDER}/{DATASET_TEST_FOLDER}/X_test_data.csv', index=False)
pd.DataFrame(y_test).to_csv(f'{DATASET_PATH}/{DATASET_PROCESSED_FOLDER}/{DATASET_TEST_FOLDER}/Y_test_data.csv', index=False)
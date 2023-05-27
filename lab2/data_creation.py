import os
import random
import datetime
import numpy as np
import pandas as pd
from settings import (
    DATASET_PREFIX, DATASET_PATH, DATASET_TRAIN_FOLDER,
    DATASET_TEST_FOLDER, DATASET_RAW_FOLDER
)

if not os.path.exists(f'{DATASET_PREFIX}/{DATASET_PATH}/{DATASET_RAW_FOLDER}'):
    os.makedirs(f'{DATASET_PREFIX}/{DATASET_PATH}/{DATASET_RAW_FOLDER}')

if not os.path.exists(f'{DATASET_PREFIX}/{DATASET_PATH}/{DATASET_RAW_FOLDER}/{DATASET_TRAIN_FOLDER}'):
    os.makedirs(f'{DATASET_PREFIX}/{DATASET_PATH}/{DATASET_RAW_FOLDER}/{DATASET_TRAIN_FOLDER}')

if not os.path.exists(f'{DATASET_PREFIX}/{DATASET_PATH}/{DATASET_RAW_FOLDER}/{DATASET_TEST_FOLDER}'):
    os.makedirs(f'{DATASET_PREFIX}/{DATASET_PATH}/{DATASET_RAW_FOLDER}/{DATASET_TEST_FOLDER}')

def generate_random(number, count):
    noise_indexes = [];

    for x in range(number):
        noise_index = random.randrange(0, count, 1)

        if noise_index not in noise_indexes:
            noise_indexes.append(noise_index)

    return noise_indexes

# Генерация тренировочных данных
year_2022_temp = np.random.normal(25, 5, 365);
year_2022_days = range(1, 366)

train_data = pd.DataFrame({ 'year_day': year_2022_days, 'day_temp': year_2022_temp })

for x in generate_random(5, 365):
    train_data.loc[x, 'day_temp'] = random.uniform(0, 1)

train_data.to_csv(f'{DATASET_PREFIX}/{DATASET_PATH}/{DATASET_RAW_FOLDER}/{DATASET_TRAIN_FOLDER}/train_data.csv', index=False)

# Генерация тестовых данных
year_2023_temp = np.random.normal(25, 5, 31);
year_2023_days = range(1, 32)

test_data = pd.DataFrame({ 'year_day': year_2023_days, 'day_temp': year_2023_temp })

for x in generate_random(2, 31):
    test_data.loc[x, 'day_temp'] = random.uniform(0, 1)

test_data.to_csv(f'{DATASET_PREFIX}/{DATASET_PATH}/{DATASET_RAW_FOLDER}/{DATASET_TEST_FOLDER}/test_data.csv', index=False)
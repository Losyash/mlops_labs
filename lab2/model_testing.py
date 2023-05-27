import pandas as pd
import pickle
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from settings import DATASET_PATH, DATASET_TEST_FOLDER, DATASET_PROCESSED_FOLDER, MODEL_PATH

X_test = pd.read_csv(f'{DATASET_PATH}/{DATASET_PROCESSED_FOLDER}/{DATASET_TEST_FOLDER}/X_test_data.csv')
Y_test = pd.read_csv(f'{DATASET_PATH}/{DATASET_PROCESSED_FOLDER}/{DATASET_TEST_FOLDER}/Y_test_data.csv')

with open(f'{MODEL_PATH}/model.pickle', 'rb') as f:
    model = pickle.load(f)

    Y_predicted = model.predict(X_test)
    mse =  mean_squared_error(Y_test, Y_predicted)

    print(f'Model square error is : {round(mse, 2)}')
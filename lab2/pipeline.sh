#!/bin/env bash

if ! [ -d logs ]; then mkdir logs; fi

echo "Start data_creation.py"
python data_creation.py

echo "Start data_preprocessing.py"
python data_preprocessing.py 

echo "Start model_preparation.py"
python model_preparation.py

echo "Start model_preparation.py"
python model_testing.py
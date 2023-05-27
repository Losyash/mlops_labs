#!/bin/env bash

if ! [ -d lab2/logs ]; then mkdir lab2/logs; fi

echo "Start data_creation.py"
python lab2/data_creation.py

echo "Start data_preprocessing.py"
python lab2/data_preprocessing.py 

echo "Start model_preparation.py"
python lab2/model_preparation.py

echo "Start model_preparation.py"
python lab2/model_testing.py
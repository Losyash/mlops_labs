#!/bin/env bash

if conda env list | grep -q lab1; then echo "Environment already exists"; else conda create -y -n lab1 python=3.10; fi

source ~/miniconda3/etc/profile.d/conda.sh
conda activate lab1

pip install numpy pandas scikit-learn

cd ~/mlops_labs/lab1

if ! [ -d logs ]; then mkdir logs; fi

echo "Start data_creation.py"
python data_creation.py > logs/lab1.log

echo "Start data_preprocessing.py"
python data_preprocessing.py > logs/lab1.log

echo "Start model_preparation.py"
python model_preparation.py > logs/lab1.log

echo "Start model_preparation.py"
python model_testing.py > logs/lab1.log
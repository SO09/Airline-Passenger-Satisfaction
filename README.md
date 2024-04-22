
# Airline Passenger Satisfaction Prediction

## Overview
This repository contains the machine learning code and datasets used to predict airline passenger satisfaction. The project utilizes a deep learning model to analyze flight experience data and predict passenger satisfaction levels. This work is based on a challenge from Kaggle, which can be accessed [here](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction).

## Dataset
The dataset includes various features related to the flight experience of passengers. The preprocessing steps include encoding categorical variables and handling missing values, especially in the 'Arrival Delay in Minutes' column by replacing them with the median value.

## Model Architecture
The model is a sequential neural network with:
- Input layer
- Four dense layers with 128, 64, 32 neurons respectively, and ReLU activation functions.
- Dropout layers to prevent overfitting, with a dropout rate of 0.5.
- The output layer with a single neuron using a sigmoid activation function suitable for binary classification.

## Training
The model is compiled using the Adam optimizer with a learning rate of 0.001. The loss function used is binary cross-entropy, and the performance metric is accuracy. The model was trained for 20 epochs with a batch size of 64.

## Performance
The model achieved a test accuracy of 96.02%, with detailed performance metrics including precision, recall, F1-score for both classes:
- Class 0 (Not Satisfied): Precision - 0.95, Recall - 0.98, F1 - 0.96
- Class 1 (Satisfied): Precision - 0.97, Recall - 0.94, F1 - 0.95

## Files and Folders
- `data/`: Folder containing the training and test datasets.
- `notebooks/`: Jupyter notebooks for exploratory data analysis and model training.


## Requirements
- Python 3.x
- TensorFlow 2.x
- Pandas
- Numpy
- Matplotlib
- Seaborn

## Contributors
- Sofiane EL FARTASS


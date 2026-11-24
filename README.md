# Diabetes-Prediction-Logistic-Regression
Machine Learning project using Logistic Regression to predict diabetes based on medical measurements.

Live demo: https://diabetes-prediction-logistic-regression-zi8fnjyndz2tsdsbfcxzup.streamlit.app/ 
# Diabetes Prediction Using Logistic Regression

## Project Overview

This project uses Logistic Regression to predict whether a person is diabetic or non-diabetic based on health-related input features.

## Objective

To build a classification model, evaluate its performance, compare original and balanced Logistic Regression, and study the effect of different decision thresholds.

## Dataset

Diabetes Prediction Dataset containing 100,000 records and the following features:

- Gender
- Age
- Hypertension
- Heart disease
- Smoking history
- BMI
- HbA1c level
- Blood glucose level
- Diabetes (target variable)

  Link: https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset 

## Technologies Used

- Python
- Google Colab
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Streamlit

## Work Completed

1. Dataset loading and exploration
2. Data cleaning and duplicate removal
3. Exploratory Data Analysis and visualizations
4. Numerical feature scaling
5. Categorical feature encoding
6. Train-test splitting
7. Original Logistic Regression model
8. Balanced Logistic Regression model
9. Model evaluation using confusion matrix, accuracy, precision, recall and F1-score
10. ROC-AUC evaluation
11. Decision threshold comparison and tuning

## Key Results

**Original Logistic Regression:**

- Accuracy: 95.97%
- Precision: 86.99%
- Recall: 63.86%
- F1-score: 73.65%
- ROC-AUC: 0.9599

**Balanced Logistic Regression:**

- Accuracy: 88.44%
- Precision: 42.50%
- Recall: 87.97%
- F1-score: 57.31%

**Tuned Decision Threshold:**

- Selected threshold: 0.8837
- Accuracy: 95.64%
- Precision: 80.86%
- Recall: 66.27%
- F1-score: 72.85%

## Repository Contents

- Jupyter Notebook with executed code and outputs
- Dataset used for model training
- Streamlit application code (if included)

## Important Note

This project is developed for educational purposes only. It is not a medical diagnostic tool.

## Reference

[https://github.com/tanvipharade](https://github.com/tanvipharade)


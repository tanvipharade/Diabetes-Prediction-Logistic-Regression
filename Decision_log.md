# Decision Log – Diabetes Prediction Using Logistic Regression

## Decision 1: Dataset Selection
I selected the Diabetes Prediction Dataset because it contains health-related features such as age, BMI, HbA1c level, blood glucose level and medical history.

## Decision 2: Data Preprocessing
I removed duplicate records, scaled numerical features and encoded categorical features to prepare the dataset for Logistic Regression.

## Decision 3: Class Balancing
I compared the original Logistic Regression model with a balanced model using `class_weight='balanced'`. I made this decision because the dataset had significantly more non-diabetic records than diabetic records.

## Decision 4: Error Type
I considered false negatives important because they represent actual diabetic cases incorrectly predicted as non-diabetic. The balanced model improved recall from 63.86% to 87.97%, although it increased false positives.

## Decision 5: Decision Threshold
I tested a threshold of 0.8837 to improve the precision-recall balance. However, I retained the original model as the best overall

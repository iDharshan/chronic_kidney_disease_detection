# -*- coding: utf-8 -*-
"""Chronic_kidney_disease_detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18RUFfliwNJ_Mdo5PdQGn9NAxMFAFQGUX
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as pltz
from sklearn.model_selection import train_test_split
from google.colab import files
uploaded = files.upload()

data=pd.read_csv("kidney_disease.csv")
data.head(5)

data.drop('id',axis=1,inplace=True)
data.info()

data.isnull().sum()

print(data['rbc'].unique())
print("############################")
print(data['pc'].unique())
print("############################")
print(data['pcc'].unique())
print("############################")
print(data['ba'].unique())
print("############################")
print(data['pcv'].unique())
print("############################")
print(data['wc'].unique())
print("############################")
print(data['rc'].unique())
print("############################")
print(data['htn'].unique())
print("############################")
print(data['dm'].unique())
print("############################")
print(data['cad'].unique())
print("############################")
print(data['appet'].unique())
print("############################")
print(data['pe'].unique())
print("############################")
print(data['ane'].unique())
print("############################")
print(data['classification'].unique())

data=data.replace({'\t':np.nan , '\t43':43,'\t6200':6200 , '\t8400':8400, '\t?':np.nan,'ckd\t':"ckd","\tyes":"yes","\tno":"no"," yes":"yes"})

print(data['rbc'].unique())
print("############################")
print(data['pc'].unique())
print("############################")
print(data['pcc'].unique())
print("############################")
print(data['ba'].unique())
print("############################")
print(data['pcv'].unique())
print("############################")
print(data['wc'].unique())
print("############################")
print(data['rc'].unique())
print("############################")
print(data['htn'].unique())
print("############################")
print(data['dm'].unique())
print("############################")
print(data['cad'].unique())
print("############################")
print(data['appet'].unique())
print("############################")
print(data['pe'].unique())
print("############################")
print(data['ane'].unique())
print("############################")
print(data['classification'].unique())

data.info()

num_cols = ['age', 'bp', 'sg', 'al', 'su', 'bgr', 'bu', 'sc', 'sod', 'pot', 'hemo']

for col in num_cols:
    data[col].fillna(data[col].mean(), inplace=True)

cat_cols = ['rbc', 'pc', 'pcc', 'ba', 'pcv', 'wc', 'rc', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane']

for col in cat_cols:
    data[col].fillna(method='backfill', inplace=True)

data.isnull().sum()

import seaborn as sns
import matplotlib.pyplot as plt
sns.boxplot(x='age', data=data)
plt.title('Box Plot of Age')
plt.show()

import seaborn as sns
sns.histplot(x='bgr', data=data, kde=True)
plt.title('Histogram of Blood Glucose Random')
plt.show()

from sklearn.preprocessing import LabelEncoder

cat_cols = ['sg', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane', 'classification']

# Create an instance of LabelEncoder
label_encoder = LabelEncoder()

# Encode categorical columns
for col in cat_cols:
    data[col] = label_encoder.fit_transform(data[col].astype(str))

data.head()

import seaborn as sns
sns.countplot(x='classification', data=data)
plt.title('Bar Plot of Class')
plt.show()

import seaborn as sns

sns.scatterplot(x='hemo', y='bp', data=data)
plt.title('Scatter Plot of Hemoglobin and Packed Cell Volume')
plt.show()

import seaborn as sns
corr_matrix = data.corr()
plt.figure(figsize=(12,10))

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.show()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

X = data.drop('classification', axis=1)
y = data['classification']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression
lr = LogisticRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
lr_acc = accuracy_score(y_test, lr_pred)
lr_cm = confusion_matrix(y_test, lr_pred)
lr_acc

# SVM
svm = SVC()
svm.fit(X_train, y_train)
svm_pred = svm.predict(X_test)
svm_acc = accuracy_score(y_test, svm_pred)
svm_cm = confusion_matrix(y_test, svm_pred)
svm_acc

# Random Forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_acc = accuracy_score(y_test, rf_pred)
rf_cm = confusion_matrix(y_test, rf_pred)
rf_acc

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
knn_acc = knn.score(X_train, y_train)
print("KNN's Accuracy is: ", knn_acc)

print("Logistic Regression Accuracy:", lr_acc)
print("SVM Accuracy:", svm_acc)
print("KNN Accuracy:", knn_acc)
print("Random Forest Accuracy:", rf_acc)

import matplotlib.pyplot as plt

# Define the accuracy values for each model
accuracy_values = [lr_acc,svm_acc,knn_acc,rf_acc]

# Define the labels for each model
model_labels = ['Logistic Regression', 'SVM', 'KNN', 'Random Forest']

# Plot a bar graph
plt.bar(model_labels, accuracy_values)

# Add a title and labels to the plot
plt.title('Accuracy Comparison of Different Models')
plt.xlabel('Model')
plt.ylabel('Accuracy')

# Display the plot
plt.show()
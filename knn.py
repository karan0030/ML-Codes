# -*- coding: utf-8 -*-
"""knn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1quj24OozTkbwTV5r_jQsVZpgpj8d_iN3

#KNN

#Imports
"""

import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split 
from collections import Counter
import matplotlib.pyplot as plt

"""#Data Load"""

#data = pd.read_csv("Iris.csv")  
data =pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

data.head()
data.shape

X = data.to_numpy()                      
X = X[:,1:data.shape[1]-1]

Y = data.to_numpy() 
Y = Y[:,data.shape[1]-1]

X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3) 

X.shape

"""#Euclidean Distance"""

def edist(x,y):
  #return np.sqrt(np.sum((x-y))**2)
  return np.linalg.norm(x-y)

"""#KNN"""

k=5
prediction = []   
correct_count = 0  
for i in range(len(X_test)): 
  distances = []
  for j in range(len(X_train)):
    dist= edist(X_test[i],X_train[j])
    distances.append((X_train[j], dist, y_train[j])) 
           
      
  distances.sort(key=lambda x: x[1])
  neighbors = distances[:k] 
  class_counter = Counter() 
  for neighbor in neighbors:
    class_counter[neighbor[2]] += 1
  prediction.append(class_counter.most_common(1)[0][0])
  if(y_test[i] == prediction[i]):
    correct_count = correct_count + 1

acc = correct_count/float(len(X_test))  

acc
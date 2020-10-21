# -*- coding: utf-8 -*-
"""linearRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MVDrT6O5GcXU0r6S7mYikXA6AmoTEijY
"""

import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split 
from collections import Counter
import matplotlib.pyplot as plt

data = pd.read_csv("headbrain.csv")

data.head()

X=data["Head Size(cm^3)"].values
Y=data["Brain Weight(grams)"].values

mean_x =np.mean(X)
mean_y =np.mean(Y)

n = len(X)

num = 0
deno = 0

for i in range(n):
  num += (X[i] - mean_x)*(Y[i] - mean_y)
  deno += (X[i] -mean_x)**2

b1 = num/deno
b0 = mean_y -(b1 * mean_x)

print(b1,b0)

max_x = np.max(X)+100
min_x =np.min(X)-100

x= np.linspace(min_x,max_x,1000)
y= b0+b1*x

plt.plot(x,y,color="red",label="linear regression")
plt.scatter(X,Y,c="blue")
plt.xlabel("head size")
plt.ylabel("brain weight")

plt.legend()
plt.show()

ss_t =0
ss_r=0
for i in range(n):
  y_pred =b0 + b1*X[i]
  ss_t += (Y[i] -mean_y)**2
  ss_r += (Y[i] -y_pred)**2
  
r2= 1-(ss_r/ss_t)
r2


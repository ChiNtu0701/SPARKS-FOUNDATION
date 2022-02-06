# -*- coding: utf-8 -*-
"""TASK 1-SPARKS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N0xcctUx8Qo4CYjRbYuFDo-1Mja9YyV1
"""

!pip install --upgrade pandas-datareader

# Commented out IPython magic to ensure Python compatibility.
#importing required libraries
import math
import pandas as pd   
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

#Implementing the model
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()

# Reading dataframe
url = "http://bit.ly/w-data"
df = pd.read_csv(url)
df.tail()

#Plotting the data
df.plot(x='Hours',y='Scores',style='d',color='g')
plt.xlabel('Hours Studied',color='#161bb8')  
plt.ylabel('Percentage Score',color='#7f42cf')  
plt.show()

#X and y values
X = df.iloc[:, :-1].values  
y = df.iloc[:, 1].values  
y

from sklearn.model_selection import train_test_split
# Create training and test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state = 0)

regressor.fit(X_train, y_train)

# Plotting the regression line
line = regressor.coef_*X+regressor.intercept_

y_pred = regressor.predict(X_test)
print(y_pred)

dfr=pd.DataFrame({'ACTUAL ':y_test,'PREDICTED ':y_pred })
dfr.head()

new_hours = np.array([[9.25]])
new_pred = regressor.predict(new_hours)
print('For 9.25 Hours :',new_pred)

import sklearn.metrics as metrics
print('MEAN ABSOLUTE ERROR: %.2f' % metrics.mean_absolute_error(y_test,y_pred))
print('MEAN SQUARED ERROR: %.2f' % metrics.mean_squared_error(y_test,y_pred))
print('ROOT MEAN SQUARED ERROR: %.2f' % math.sqrt(metrics.mean_squared_error(y_test,y_pred)))

#ACCURACY
from sklearn.metrics import r2_score
acc = r2_score(y_test, y_pred)
print(acc)
print('ACCURACY: %.2f' % acc)
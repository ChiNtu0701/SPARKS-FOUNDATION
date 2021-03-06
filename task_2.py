# -*- coding: utf-8 -*-
"""TASK-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J8sBLQU908l-vQ6V__s7njHT82PpszRA

# **Prediction using Unsupervised Machine Learning**
"""

# Commented out IPython magic to ensure Python compatibility.
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# %matplotlib inline

iris = Iris =pd.read_csv('/content/drive/MyDrive/Iris.csv')
iris.head()

# Check if there any null value in the Dataset
iris.isnull == True

iris.columns

iris.dtypes

iris.info

# Dividing this into Independent and dependent features
x=iris.iloc[:, [1,4]].values

from sklearn.cluster import KMeans
wcss=[]
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init ='k-means++', random_state =42) # We use k-means++ to avoid the random initialization trap
    kmeans.fit(x)
    wcss.append(kmeans.inertia_) # kmeans.inertia_ returns the WCSS value for an initialized cluster
plt.plot(range(1, 11), wcss, color='#9c71a6')
plt.title('The elbow Method', color='#a34061')
plt.xlabel('Number of clusters', color='#2f0070')
plt.ylabel('WCSS', color='#2f0070')
plt.show()

kmeans = KMeans(n_clusters = 3, init ='k-means++', random_state = 42)
y_kmeans=kmeans.fit_predict(x)
y_kmeans

# Visualising the clusters - On the first two columns
plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s = 100, c = '#9c71a6', label = 'Iris-setosa')
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s = 100, c = '#a34061', label = 'Iris-versicolour')
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1],s = 100, c = '#2f0070', label = 'Iris-virginica')
predictedY = np.choose(y_kmeans, [1, 0, 2]).astype(np.int64)
# Plotting the centroids of the clusters
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s = 100, c = 'purple', label = 'Centroids')
plt.title('Cluster of Iris Data')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.show()
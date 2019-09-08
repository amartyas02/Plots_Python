fig, ax = plt.subplots()

'''Simple scatter plot'''
ax.scatter(iris['sepal_length'], iris['sepal_width'])

ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')

'''Coloring each data point by its class in scatter plot.'''

# create color dictionary
colors = {'Iris-setosa':'r', 'Iris-versicolor':'g', 'Iris-virginica':'b'} #iris[Class] available with elements 'Iris-setosa', etc.


fig, ax = plt.subplots()
# plot each data-point
for i in range(len(iris['sepal_length'])):
    ax.scatter(iris['sepal_length'][i], iris['sepal_width'][i],color=colors[iris['class'][i]])
# set a title and labels
ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')

'''Simple Line Chart'''

x_data = range(0, iris.shape[0])
fig, ax = plt.subplots()
# plot Multiple Columns in the same graph 

for column in columns:
    ax.plot(x_data, iris[column])
# set title and legend
ax.set_title('Iris Dataset')
ax.legend()

'''Simple Histogram'''

 # If we pass it categorical data like the points column from the wine-review dataset it will automatically calculate how often each class occurs.

fig, ax = plt.subplots()
# plot histogram
ax.hist(wine_reviews['points'])
# set title and labels
ax.set_title('Wine Review Scores')
ax.set_xlabel('Points')
ax.set_ylabel('Frequency')

 # The bar-chart isn’t automatically calculating the frequency of a category so we are going to use pandas value_counts function to do this. 
 # The bar-chart is useful for categorical data that doesn’t have a lot of different categories

fig, ax = plt.subplots() 
# count the occurrence of each class 
data = wine_reviews['points'].value_counts() 
# get x and y data 
points = data.index 
frequency = data.values 
# create bar chart 
ax.bar(points, frequency) 
# set title and labels 
ax.set_title('Wine Review Scores') 
ax.set_xlabel('Points') 
ax.set_ylabel('Frequency')

'''Plotting Heatmap'''

import numpy as np
import seaborn as sns

# get correlation matrix
corr = iris.corr()
fig, ax = plt.subplots()
# create heatmap
im = ax.imshow(corr.values)

# set labels
ax.set_xticks(np.arange(len(corr.columns)))
ax.set_yticks(np.arange(len(corr.columns)))
ax.set_xticklabels(corr.columns)
ax.set_yticklabels(corr.columns)

# Loop over data dimensions and create text annotations.
for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        text = ax.text(j, i, np.around(corr.iloc[i, j], decimals=2),
                       ha="center", va="center", color="black")

'''Pairplot'''

#plot a grid of pairwise relationships in a dataset.
sns.pairplot(iris, hue = 'sex') #Hue colors according to the column name given.

#OR

from pandas.plotting import scatter_matrix

fig, ax = plt.subplots(figsize=(12,12))
scatter_matrix(iris, alpha=1, ax=ax)

'''BoxPlot'''

sns.boxplot('points', 'price', data=df)



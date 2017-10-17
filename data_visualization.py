import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

import logging
import json

logging.basicConfig(filename='example.log', level=logging.DEBUG)
# logging.debug('This message should go to the log file')
#logging.info('So should this')
# logging.warning('And this, too')

# t-distributed Stochastic Neighbor Embedding (t-SNE) visualization
from sklearn.manifold import TSNE
# visulaize the important characteristics of the dataset
import matplotlib.pyplot as plt

# step 1: download the data
# dataframe_all = pd.read_csv("https://d396qusza40orc.cloudfront.net/predmachlearn/pml-training.csv")
dataframe_all = pd.read_csv('pml-training.csv')
num_rows = dataframe_all.shape[0]

logging.info("num_rows:" + json.dumps(num_rows));

# step 2: remove useless data
# count the number of missing elements (NaN) in each column
counter_nan = dataframe_all.isnull().sum()
# logging.info("counter_nan:" + json.dumps(counter_nan));

counter_without_nan = counter_nan[counter_nan == 0]

# logging.info("counter_without_nan:" +json.dumps( counter_without_nan));

# remove the columns with missing elements
dataframe_all = dataframe_all[counter_without_nan.keys()]
# remove the first 7 columns which contain no discriminative information
dataframe_all = dataframe_all.ix[:, 7:]
# the list of columns (the last column is the class label)
columns = dataframe_all.columns
# logging.info("columns:" +json.dumps( columns));


# step 3: get features (x) and scale the features
# get x and convert it to numpy array
x = dataframe_all.ix[:, :-1].values
standard_scaler = StandardScaler()
x_std = standard_scaler.fit_transform(x)

# print x;
# print x_std;

# step 4: get class labels y and then encode it into number
# get class label data
y = dataframe_all.ix[:, -1].values

print y;
# encode the class label
class_labels = np.unique(y)
print class_labels;

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)
print y;

# step 5: split the data into training set and test set
test_percentage = 0.1
x_train, x_test, y_train, y_test = train_test_split(x_std, y, test_size=test_percentage, random_state=0)

print x_train;
print x_test;
print y_train;
print y_test;

tsne = TSNE(n_components=2, random_state=0)
x_test_2d = tsne.fit_transform(x_train)
print x_test_2d;

ruf = x_test_2d[y_train == 1, 0];

# scatter plot the sample points among 5 classes
markers = ('s', 'd', 'o', '^', 'v')
color_map = {0: 'red', 1: 'blue', 2: 'lightgreen', 3: 'purple', 4: 'cyan'}
plt.figure()
for idx, cl in enumerate(np.unique(y_test)):
    plt.scatter(x=x_test_2d[y_train == cl, 0], y=x_test_2d[y_train == cl, 1], c=color_map[idx], marker=markers[idx],
                label=cl)
plt.xlabel('X in t-SNE')
plt.ylabel('Y in t-SNE')
plt.legend(loc='upper left')
plt.title('t-SNE visualization of test data')
plt.show()

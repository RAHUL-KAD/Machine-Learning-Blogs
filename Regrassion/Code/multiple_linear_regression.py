
# importing the libraries
import numpy as np
import pandas as pd

# importing the dataset
dataset = pd.read_csv('name_of_dataset.csv')
# droping the unnecessary columns
dataset.drop(['Name','Author'], axis=1, inplace=True)
# independent variables
X = dataset.iloc[:, :-1].values
# dependent variables
y = dataset.iloc[:, -1:].values

"""Encoding categorical data"""

# importing scikit learn library
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [2])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

"""Spliting the dataset into training and testing dataset"""

# imporiting necessary library and it's module
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

"""Training the data"""

# importing the library
from sklearn.linear_model import LinearRegression
# creating an object of class LinearRegression
LR = LinearRegression()
# Fitting our training data to train the model
LR.LR.fit(X_train, y_train)

# predicting the test result
y_pred = LR.predict(X_test)

# creating new dataframe
df = pd.DataFrame({'Real Value':y_test, 'predictated value':y_pred})
df

# coefficient of X
coefficient = LR.coef_
# Interceptor of y
interceptor = LR.intercept_

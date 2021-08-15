# pandas is built on top of numpy

## Series

import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)

"""
Pandas Series is a one-dimensional labeled array capable of holding data
of any type (integer, string, float, python objects, etc.). The axis labels
are collectively called index. Pandas Series is nothing but a column in an excel sheet.
Labels need not be unique but must be a hashable type.
"""

my_series = pd.Series(data=my_data, index=labels)
print(my_series)

my_series = pd.Series(my_data,labels)
print(my_series)

## Dataframes

"""
DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.
You can think of it like a spreadsheet or SQL table, or a dict of Series objects.
It is generally the most commonly used pandas object.
DataFrames comprise of Series.
"""

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])

print(df['W']) # getting a column from a dataframe
print(df[['W','X']]) # to get multiple columns, pass in a list of column names
print(type(df)) # DataFrame
print(type(df['W'])) # Series, dataframes are made up of Series
print(type(df[['W','X']])) # Series, dataframes are made up of Series

print(df.loc['A']) # returns a series for the queried row
print(df.iloc[0]) # returns a series for the queried row by index

# adding a column
df['new1'] = 5 # this add a new row with 5 to every row
df['new2'] = df['W'] + df['Y'] # add a new row with arithematic

print(df)

# dropping a column
df = df.drop('new1',axis=1) # not happening in place
# df = df.drop('new1',axis=1,inplace=True) # happening in place

print(df)

# dropping a row
df = df.drop('E')

print(df)

# get dataframe dimensions
print(df.shape)

# get subset of rows and columns
print(df.loc['B','Y']) # get single value
subset_df = df.loc[['A','B'],['W','Y']] # get a dataframe which is a subset of the original
print(subset_df) # get a dataframe which is a subset of the original

# conditional selection
print(df)

print(df > 0) # returns df of booleans
print(df[df > 0]) # returns masked data
print(df[df['W'] > 0]) # get back entire rows/records where W > 0
print(df[df['Z'] < 0]) # get back entire rows/records where Z > 0
print(df[df['Z'] < 0][['X', 'Y']]) # get back X and Y columns of rows/records where Z > 0

# multiple conditions
print(df)

print(df[(df['W'] > 0) | (df['Y'] > 1)]) # do NOT use python's normal 'and' or 'or' operators
print(df[(df['W'] > 0) & (df['Y'] > 1)]) # do NOT use python's normal 'and' or 'or' operators
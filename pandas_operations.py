import numpy as np
import pandas as pd

df = pd.DataFrame({
    'col1': [1,2,3,4],
    'col2': [444,555,666,444],
    'col3': ['abc','def','ghi','xyz']
})

print(df)

print(df['col2'].unique()) # get unique values from a column
print(df['col2'].nunique()) # get count of unique values from a column
print(df['col2'].value_counts()) # get unique values and their counts from a column

# apply

def times2(x):
    return x * 2

df['col4'] = df['col1'].apply(times2)

print(df)

# apply with lambda function

print(df['col2'].apply(lambda x: x * 2))

# get df attributes

print(df.columns)
print(df.index)

# sorting df

print(df.sort_values(by='col2'))

# finding null values

print(df.isnull()) # return df of booleans

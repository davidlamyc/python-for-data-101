import numpy as np
import pandas as pd

# create df from dictionary
d = {'A': [1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}

df = pd.DataFrame(d)

print(df)

print(df.dropna()) # drop rows with one or more missing values
print(df.dropna(axis=1)) # drop columns with one or more missing values
print(df.dropna(thresh=2)) # drop rows with one or more missing values

print(df.fillna(value='FILL')) # fill all na
print(df['A'].fillna(value=df['A'].mean())) # fill all na 
"""
Solutions are intended to have repetitive code,
so each solution more or less stands on its own
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# a. b.
df = pd.read_csv('Movies.csv')

print(df)
print(df.dtypes)

# c.
df["Studio"] = df["Studio"].astype('category')

# d.
oq_map = {
    'OpenQuarter': {
        1: '1st',
        2: '2nd',
        3: '3rd',
        4: '4th'
    }
}

df = df.replace(oq_map)

# e.
print(df[df['Studio'] == 'Disney'].count()) # answer: 5

# f.
print(df.sort_values(by='TopGross',ascending=False).head(10)[df['Studio'] == 'Disney'].count()) # answer: 4

# g.
print(df[df['Studio'] == 'Disney'].sum()) # answer: 2039 million

# h.
print(df.sort_values(by='TopGross',ascending=False).head(10)[df['Studio'] == 'Disney'].sum()) # answer: 1829 million

# i.
print(df.sort_values(by='TopGross',ascending=False).head(5)[df['Studio'] == 'Disney'].sum()) # answer: 1514 million

# j.
print(df[df['Studio'] == 'Warner']) 
print(df[df['Studio'] == 'Warner'].count()) # answer: 4

# k.
print(df.sort_values(by='TopGross',ascending=False).head(10)[df['Studio'] == 'Warner'].count()) # answer: 3

# l.
print(df[df['Studio'] == 'Warner'].sum()) # answer: 1158 million

# m.
print(df.sort_values(by='TopGross',ascending=False).head(10)[df['Studio'] == 'Warner'].sum()) # answer: 970 million

# n.
print(df.sort_values(by='TopGross',ascending=False).head(5)[df['Studio'] == 'Warner'].sum()) # answer: 413 million

# o.
sns.countplot(x='Studio',data=df)

plt.show()

# p.
sns.countplot(x='Studio',data=df.sort_values(by='TopGross',ascending=False).head(10))

plt.show()




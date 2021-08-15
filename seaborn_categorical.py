import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# load dataset
tips = sns.load_dataset('tips')

print(tips.head())

# sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std) # estimator is mean by default

# sns.countplot(x='sex',data=tips)

# box plot and violin plot to show distribution

# sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker')

sns.violinplot(x='day',y='total_bill',data=tips)


plt.show()
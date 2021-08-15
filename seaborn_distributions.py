import seaborn as sns
import matplotlib.pyplot as plt

# load dataset
tips = sns.load_dataset('tips')

print(tips.head())

sns.displot(tips['total_bill'], kde=False,bins=30) # kde=False removes kernel density line

sns.jointplot(x='total_bill',y='tip',data=tips)
# sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')
# sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg') # regression line with jointplot
# sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde')

sns.pairplot(tips,hue='sex',palette='coolwarm')

plt.show()
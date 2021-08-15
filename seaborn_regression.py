import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
# tips.head()

# sns.lmplot(x='total_bill',y='tip',data=tips)
# sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex')
sns.lmplot(x='total_bill',y='tip',data=tips,col='sex')

plt.show()
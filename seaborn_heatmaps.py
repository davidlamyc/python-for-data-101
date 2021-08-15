import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

print(tips.head())
print(flights.head())

tc = tips.corr()
print(tc)

# sns.heatmap(tc,annot=True)

sns.heatmap(tc,cmap='magma',linecolor='white',linewidths=3)

plt.show()


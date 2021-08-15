import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

print(iris.head())
print(iris['species'].unique())

# sns.pairplot(iris)
g = sns.PairGrid(iris)
g.map(plt.scatter)

plt.show()
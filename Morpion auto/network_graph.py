import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import (DecisionTreeClassifier, plot_tree)

iris = load_iris()
print(iris.data, iris.target)

tree = DecisionTreeClassifier().fit(iris.data,iris.target)

plot_tree(tree)
plt.show()
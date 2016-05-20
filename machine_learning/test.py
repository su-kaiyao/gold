# -*- coding: utf-8 -*-

'''
Supervised Learning - Classification
'''

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

def plot_2d_separator(classifier, X, fill=False, ax=None, eps=None):
    if eps is None:
        eps = X.std() / 2.
    x_min, x_max = X[:, 0].min() - eps, X[:, 0].max() + eps
    y_min, y_max = X[:, 1].min() - eps, X[:, 1].max() + eps
    xx = np.linspace(x_min, x_max, 100)
    yy = np.linspace(y_min, y_max, 100)

    X1, X2 = np.meshgrid(xx, yy)
    X_grid = np.c_[X1.ravel(), X2.ravel()]
    try:
        decision_values = classifier.decision_function(X_grid)
        levels = [0]
        fill_levels = [decision_values.min(), 0, decision_values.max()]
    except AttributeError:
        # no decision_function
        decision_values = classifier.predict_proba(X_grid)[:, 1]
        levels = [.5]
        fill_levels = [0, .5, 1]

    if ax is None:
        ax = plt.gca()
    if fill:
        ax.contourf(X1, X2, decision_values.reshape(X1.shape),
                    levels=fill_levels, colors=['blue', 'red'])
    else:
        ax.contour(X1, X2, decision_values.reshape(X1.shape), levels=levels,
                   colors="black")
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xticks(())
    ax.set_yticks(())

'''
First, we look at a two class classification problem in two dimensions.
We use the synthetic data generated by the make_blob function.
'''
X, y = make_blobs(centers=2, random_state=0)

# print (X.shape)
# print (y.shape)
# print (X[:5,:])
# print (y[:5])

# plt.scatter(X[:,0], X[:,1], c=y, s=40)
# plt.xlabel("first feature")
# plt.ylabel("second feature")
# plt.show()
'''
The train_test_split function randomly split 25% of the data for testing.
'''
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
# print X_train.shape
# print X_test.shape

# logistic regressions
classifier = LogisticRegression()
# call fit cunction with the training data, and the corresponding trainging labels
classifier.fit(X_train, y_train)
# apply the model to unseen data
prediction = classifier.predict(X_test)
# print (prediction)
# print (y_test)
'''
evaluate our classifier quantitatively by measuring what fraction of predicitons is correct.
This is called accuracy.
'''
# print np.mean(prediction == y_test)
'''
A more convenience function: score
all scikit-learn classifiers have to compute this directly from the test data.
'''
# print classifier.score(X_test, y_test)
# print classifier.score(X_train, y_train)

plt.scatter(X[:,0], X[:,1], c=y, s=40)
plt.xlabel("first feature")
plt.ylabel("second feature")
plot_2d_separator(classifier, X)
plt.show()

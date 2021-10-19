import matplotlib.pyplot as plt
import cec2017
import numpy as np

from cec2017.functions import f1

MAX_X = 100
PLOT_STEP = 0.1

x_arr = np.arange(-MAX_X, MAX_X, PLOT_STEP)
y_arr = np.arange(-MAX_X, MAX_X, PLOT_STEP)
X, Y = np.meshgrid(x_arr, y_arr)
Z = np.empty(X.shape)

f=f1

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Z[i, j] = f(np.array([X[i, j], Y[i, j]]))

cp = plt.contour(X, Y, Z, 20)
plt.arrow(0, 0, 50, 50, head_width=5, head_length=10, fc='k', ec='k')
plt.show()
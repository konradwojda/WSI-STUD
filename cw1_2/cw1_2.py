import numpy as np
import matplotlib.pyplot as plt
from cec2017.functions import f1, f2, f3
import numdifftools as nd

def partial_derivative(f, x: np.array, n: int):
    dx = 1e-6
    new = x.copy()
    new[n] = x[n] + dx
    diff = (f(new) - f(x))
    return diff / dx

def gradient(f, x: np.array):
    return np.array([partial_derivative(f, x, var) for var in range(x.size)])

"""
f - function
b - learning rate (beta)
x - starting point
n - number of iterations
"""
def steepest_ascent(f, b, x: np.array, n):
    dx = x.copy()
    for _ in range(n):
        d = gradient(f, dx)
        dx2 = dx.copy()
        dx += b*d
        plt.arrow(dx2[0], dx2[1], dx[0], dx[1], head_width=5, head_length=10, fc='k', ec='k')
        print(dx)
    print(f1(dx))


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

x = np.random.uniform(-100, 100, size=2)
steepest_ascent(f1, 0.1, x, 5)
# plt.arrow(0, 0, 50, 50, head_width=5, head_length=10, fc='k', ec='k')
plt.show()
# print(partial_derivative(f1, np.array([100.0,110.0]), 1))
# print(gradient(f1, np.array([0.0,0.0])))
# print(nd.Gradient(f1)([0.0, 0.0]))
#print(gradient(f1, np.array([1.44284127e+14, 3.18767263e+14])))
# steepest_ascent(f1, 0.1, np.array([10.0, 10.0]), 100)
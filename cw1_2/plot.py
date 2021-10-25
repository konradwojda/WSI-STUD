import matplotlib.pyplot as plt
import cec2017
import numpy as np

from cec2017.functions import f1, f2, f3

def make_2d_plot(fun, points):

    MAX_POINT = max([max([abs(n) for n in x]) for x in points])
    PLOT_STEP = MAX_POINT / 200

    x_arr = y_arr = np.arange(-MAX_POINT, MAX_POINT, PLOT_STEP)
    X, Y = np.meshgrid(x_arr, y_arr)
    Z = np.empty(X.shape)

    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Z[i, j] = fun(np.array([X[i, j], Y[i, j]]))

    cp = plt.contourf(X, Y, Z, 20)

    for point in points:
        plt.plot(point[0], point[1], color='r', marker='.')

    for i in range(len(points)-1):
        delta = points[i+1] - points[i]
        plt.arrow(points[i][0], points[i][1], delta[0], delta[1], head_width=MAX_POINT * 0.015, head_length=MAX_POINT * 0.015, fc='k', ec='k')


    plt.show()
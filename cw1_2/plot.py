import matplotlib.pyplot as plt
import cec2017
import numpy as np

from cec2017.functions import f1, f2, f3

# from cw1_2 import steepest_ascent

def make_2d_plot(fun, points):

    MAX_POINT = max([max([abs(n) for n in x]) for x in points])
    PLOT_STEP = MAX_POINT / 400

    x_arr = y_arr = np.arange(-MAX_POINT, MAX_POINT, PLOT_STEP)
    X, Y = np.meshgrid(x_arr, y_arr)
    Z = np.empty(X.shape)

    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Z[i, j] = fun(np.array([X[i, j], Y[i, j]]))

    cp = plt.contour(X, Y, Z, 20)

    for point in points:
        plt.plot(point[0], point[1], color='r', marker='.')

    # for i in range(len(points)-1):
    #     plt.arrow(points[i][0], points[i][1], points[i+1][0], points[i+1][1], head_width=5, head_length=10, fc='k', ec='k')
    # plt.plot(points[-1][0], points[-1][1], color='r', marker='.')


    plt.show()
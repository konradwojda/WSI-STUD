import numpy as np
import matplotlib.pyplot as plt
from cec2017.functions import f1, f2, f3
import numdifftools as nd

from plot import make_2d_plot

UPPER_BOUND = 100
DIMENSIONALITY = 2


def booth(x: np.array):
    return (x[0] + 2*x[1] - 7)**2 + (2*x[0] + x[1] - 5)**2


def stop(fun, points: np.array, beta):
    if(len(points) > 2000):
        return True
    
    checking_point = points[-1]
    epsilon = 0.001
    checking_value = fun(checking_point)

    if(beta > 0):
        cond1 = checking_value >= fun(checking_point + np.array([0, epsilon]))
        cond2 = checking_value >= fun(checking_point + np.array([0, -epsilon]))
        cond3 = checking_value >= fun(checking_point + np.array([epsilon, 0]))
        cond4 = checking_value >= fun(checking_point + np.array([-epsilon, 0]))
        if(cond1 and cond2 and cond3 and cond4):
            return True

    elif(beta < 0):
        cond1 = checking_value <= fun(checking_point + np.array([0, epsilon]))
        cond2 = checking_value <= fun(checking_point + np.array([0, -epsilon]))
        cond3 = checking_value <= fun(checking_point + np.array([epsilon, 0]))
        cond4 = checking_value <= fun(checking_point + np.array([-epsilon, 0]))
        if(cond1 and cond2 and cond3 and cond4):
            return True


"""
f - function
b - learning rate (beta)
x - starting point
n - number of iterations
"""
def steepest_ascent(fun, b, x: np.array, n):
    point = x
    # prevPoint = point
    path = [point]
    while not stop(fun, path, b):
        point = point + (b * nd.Gradient(fun)(point))
        # print(point)
        # print(fun(point))
        # prevPoint = point
        path.append(point)
    # print(path)
    return path

def plot_steepest_ascent(fun, beta, n):
    starting_point = np.random.uniform(-UPPER_BOUND, UPPER_BOUND, size=DIMENSIONALITY)
    q = fun(starting_point)
    print(starting_point)
    print('q(x) = %.6f' %q)
    points = steepest_ascent(fun, beta, starting_point, n)
    dq = fun(points[-1])
    print(points[-1])
    print('q(x) = %.6f' %dq)
    make_2d_plot(fun, points)



if __name__ == "__main__":
    plot_steepest_ascent(f1, -0.00000001, 400)
    # plot_steepest_ascent(f2, 0.5, 40)
    # plot_steepest_ascent(f3, 0.00005, 40)
    # plot_steepest_ascent(booth, -0.05, 40)


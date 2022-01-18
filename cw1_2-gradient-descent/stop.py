import numpy as np

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
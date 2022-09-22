import matplotlib as plot
import numpy as np


# unconstrained function is distance between x2 and x3, and the point
def function(x):
    x2 = x[0]
    x3 = x[1]
    return ((-2 * x2 - 3 * x3 + 1) + 1) ** 2 + x2 ** 2 + (x3 - 1) ** 2


def gradient(x):
    x2 = x[0]
    x3 = x[1]
    return np.array([10 * x2 + 12 * x3 - 8, 20 * x3 + 12 * x2 - 14])

breakpoint()
xinit = np.array([1, -1])  # initial guess
g0 = np.array([-10, -22])  # gradient value at initial guess


t = 0.5


def ils(x,alpha):  # ils=inexact line search-- outline of code given in class
    phi = function(x) - t * gradient(x).T @ gradient(x) * alpha
    if function(x - alpha * g0) > phi:
        alpha = .5 * alpha
        return ils(x, alpha)
    else:
        return alpha

breakpoint()

while np.linalg.norm(gradient(xlistgrad[k])) > 0.000001:
    xprev = xlistgrad[k]
    alpha = 1
    alpha = ils(xprev, alpha)
    xnow = xprev - alpha * gradient(xprev)
    xlistgrad.append(xnow)
    k += 1

xx = xlistgrad[len(xlist)-1]

x2g = xx[0]
x3g = xx[1]
x1g = 1 - 2 * x2g - 3 * x3g
print("x1 = " + str(x1g))
print("x2 = " + str(x2g))
print("x3 = " + str(x3g))
print("Initial guess for x2 and x3 are:" + str(xinit))
# I was having problems with this code running in Pycharm for some reason, so I switched to Jupyter at this point, and it worked.

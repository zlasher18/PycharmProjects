import matplotlib as plot
import numpy as np

# unconstrained function is distance between x2 and x3, and the point
def function(x):
    x2 = x[0]
    x3 = x[1]
    return ((-2*x2-3*x3+1)+1)**2+x2**2+(x3-1)**2

def gradient(x):
    x2 = x[0]
    x3 = x[1]
    return np.array([10 * x2 + 12 * x3 - 8, 20 * x3 +12 * x2 - 14])

xinit = np.array([ 1, -1])  # initial guess
g0 = np.array([-10, -22]) # gradient value at initial guess

breakpoint()

t = 0.5
def ils(x,alpha):
    phi = funciton(x) - t* gradient(x).T @ gradient(x) * alpha
    if (function(x - alpha *g0) > phi):
        alpha = .5 * alpha
        return ils(x,alpha)
    else:
        return alpha




print("Initial guess for x2 and x3 are:" + str(xinit))

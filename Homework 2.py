import matplotlib as plot
import numpy as np

# unconstrained
def function(x):
    x2 = x[0]
    x3 = x[1]
    return ((-2*x2-3*x3+1)+1)**2+x2**2+(x3-1)**2

def gradient(x):
    x2 = x[0]
    x3 = x[1]
    return ([10 * x2 + 12 * x3 - 8, 20 * x3 +12 * x2 - 14])

guess1 = [ 1, -1]
g0 = [-10, -22]

breakpoint()

t = np.linspace(0, 1, 0.05)
def ile(function, g0, guess1, t):
    alpha = 1
    step = 0
    f0 = function(guess1 - alpha * g0)
    phi0 = function(guess1) - t* g0 .T @ g0 * alpha
    while f0 > phi0 and step < 100 :
        alpha = alpha / 2
        step += 1
        f0 = function(guess1 - alpha * g0)
        phi0 = function(guess1) - t* g0 .T @ g0 * alpha
    xk = guess1 - alpha * g0
    return xk

for counter

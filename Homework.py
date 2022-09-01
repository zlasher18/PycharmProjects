import scipy
import numpy
from scipy.optimize import minimize
from scipy.optimize import Bounds


def function(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    x5 = x[4]
    return (x1-x2)**2+(x2+x3-2)**2+(x4-1)**2+(x5-1)**2


const = ({'type': 'eq', 'fun': lambda x: x[0] + 3*x[1]},
         {'type': 'eq', 'fun': lambda x: x[2] + x[3] - 2*x[4]},
         {'type': 'eq', 'fun': lambda x: x[1] - x[4]})
b = Bounds([-10, -10, -10, -10, -10], [10, 10, 10, 10, 10])
guess1 = [5, 5, 5, 5, 5]

result = minimize(function, guess1, bounds=b, constraints=const)
guess2 = [-10, -10, -10, -10, -10]
res = minimize(function, guess2, bounds=b, constraints=const)
print(result)
print(res)
# Changing the guess does not change the output a significant amount.
# This suggests to me that this is truly the local minimum, but there is no way to prove this for sure.

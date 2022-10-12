from bayes_opt import BayesianOptimization


def function(x1,x2):
    return -1*((4-2.1*x1**2+x1**4/3)*x1**2+x1*x2+(-4+4*x2**2)*x2**2)
# there is no miminize in the BayesianOptimization library I found, so I multiplied the function by -1 and maximized.
# Maximizing the negative of the function is the same thing as minimizing the original.
pbounds = {'x1': (-3,3), 'x2': (-2,2)}

optimizer = BayesianOptimization(f=function,pbounds=pbounds,random_state=1)

optimizer.maximize(init_points=1203,n_iter=1203)
# The 'target' values are actually the opposite sign of what is displayed, so the minimum is 1.028.
# through trial and error with the number of iterations, I discovered that 1203 gave the minimum.
# I found this off-the-shelf Bayesian Optimization solver at https://github.com/fmfn/BayesianOptimization


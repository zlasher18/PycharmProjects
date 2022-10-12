# Homework 3
import torch as tc
import numpy as np
from torch.autograd import Variable
import matplotlib.pyplot as plt

# setting up all the variables
x1 = np.array([0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1])
x2 = np.array([1, .9, .8, .7, .6, .5, .4, .3, .2, .1, 0]) #x1+x2=1
X1 = tc.tensor(x1, requires_grad=False, dtype=tc.float32)
X2 = tc.tensor(x2, requires_grad=False, dtype=tc.float32)
aw = np.array([8.07131, 1730.63, 233.426])
ad = np.array([7.43155, 1554.679, 240.337])
T = 20
pw = 10** (aw[0] - aw[1] / (T + aw[2]))
pd = 10** (ad[0] - ad[1] / (T + ad[2]))
p = np.array([28.1,34.4,36.7,36.9,36.8,36.7,36.5,35.4,32.9,27.7,17.5])
p = tc.tensor(p, requires_grad=False, dtype=tc.float32)
A = Variable(tc.tensor([2.0, 2.0]), requires_grad=True)
breakpoint()

for i in range(100):
    p_predict = X1 * tc.exp(A[0]* (A[1] * X2 / (A[0] * X1 + A[1] * X2)) ** 2) * pw + X2 * tc.exp(A[1] * (A[0] * X1 / (A[0] * X1 + A[1] * X2)) ** 2) * pd

    error = (p_predict-p)**2 # square error
    error = error.sum()

    error.backward() #computes gradient at current iteration

    with tc.no_grad():
        alpha = .0001
        A -= alpha * A.grad # gives gradient

        A.grad.zero_()

print('Estimation of A12 and A21 are',A.data.numpy())
print('final error is',error.data.numpy())

p_predict = p_predict.detach().numpy()
p = p.detach().numpy()
X1 = X1.detach().numpy()

plt.plot(X1, p_predict, label = 'Predicted Pressure')
plt.plot(X1, p, label = 'Pressure')
plt.title('Pressure and predicted pressure vs x')

plt.legend()
plt.show()
# The predicted pressure is very close to the measured pressure.

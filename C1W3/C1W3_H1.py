from numpy import linalg
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


def f(x):
    return math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)


x = np.arange(1, 31, 0.1)
y = [f(i) for i in x]
plt.plot(x, y)
plt.show()
res = optimize.minimize(f, 30, method='BFGS')
print(res)

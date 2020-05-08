from numpy import linalg
import math
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)


l_1n_array = np.array([[1., 1.], [1., 15.]])
r_1n_array = np.array([f(1), f(15)])
answer = linalg.solve(l_1n_array, r_1n_array)

x = np.arange(1, 15, 0.1)
y = [f(i) for i in x]
y1 = [answer[0]+answer[1]*i for i in x]
plt.plot(x, y1)
plt.plot(x, y)
plt.show()


l_1n_array = np.array([[1., 1., 1.], [1., 8., 8.**2], [1., 15., 15.**2]])
r_1n_array = np.array([f(1), f(8), f(15)])
answer = linalg.solve(l_1n_array, r_1n_array)

x = np.arange(1, 15, 0.1)
y = [f(i) for i in x]
y1 = [answer[0]+answer[1]*i+answer[2]*i**2 for i in x]
plt.plot(x, y1)
plt.plot(x, y)
plt.show()


l_1n_array = np.array([[1., 1., 1., 1.], [1., 4., 4.**2, pow(4., 3)], [1., 10., 10.**2, pow(10., 3)], [1., 15., 15.**2, pow(15.,3)]])
r_1n_array = np.array([f(1), f(4), f(10), f(15)])
answer = linalg.solve(l_1n_array, r_1n_array)

x = np.arange(1, 15, 0.1)
y = [f(i) for i in x]
y1 = [answer[0]+answer[1]*i+answer[2]*i**2+answer[3]*pow(i, 3) for i in x]
plt.plot(x, y1)
plt.plot(x, y)
plt.show()

with open('sentences-2.txt', 'w') as o_file:
    o_file.write(f'{answer[0]} {answer[1]} {answer[2]} {answer[3]}')

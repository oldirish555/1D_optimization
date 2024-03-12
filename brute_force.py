import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x+4)**2+2*x # example function

def brute_force(f, a, b, step_size):
    x_min = None
    f_min = float('inf')
    x = a
    while x <= b:
        fx = f(x)
        plt.scatter(x, fx, color='green')
        if fx < f_min:
            x_min = x
            f_min = fx
        x += step_size
    return x_min

a = -10
b = 11
x = np.linspace(a, b, 100)
y = f(x)

min_x = brute_force(f, a, b, 2)
min_y = f(min_x)

plt.plot(x, y)
plt.scatter(a, f(a), color='blue')
plt.scatter(b, f(b), color='blue')
plt.scatter(min_x, min_y, color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Minimization of 1D Function by Brute Force Method')

plt.show()

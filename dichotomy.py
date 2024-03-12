import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x+4)**2+2*x # example function

def dichotomy(f, a, b, epsilon):
    while (b-a) > epsilon:
        c = (a+b)/2
        if f(c-epsilon) < f(c+epsilon):
            b = c
        else:
            a = c
    return (a+b)/2

a = -10
b = 10
x = np.linspace(a, b, 100)
y = f(x)

min_x = dichotomy(f, a, b, 0.01)
min_y = f(min_x)

plt.plot(x, y)
plt.scatter(a, f(a), color='blue')
plt.scatter(b, f(b), color='blue')
plt.scatter(min_x, min_y, color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Minimization of 1D Function by Dichotomy Method')

plt.show()

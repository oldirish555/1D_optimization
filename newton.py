import math as m 
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x+2)**4 - 7*x**2 + 2 # example function

def ff(x):
    return 4*(x+2)**3 - 14*x # first derivative

def fff(x):
    return 12*(x+2)**2 - 14 # second derivative


def newton(ff, fff, a, b, tol=1e-6):
    x = (a + b) / 2.0
    # Iterative procedure
    while abs(ff(x)) > tol:
        
        x = x - ff(x)/fff(x)

    return x


a = -10
b = 4
x = np.linspace(a, b, 100)
y = f(x)

min_x = newton(ff, fff, a, b, 0.01)
min_y = f(min_x)

plt.plot(x, y)
plt.scatter(a, f(a), color='green')
plt.scatter(b, f(b), color='red')
plt.scatter(min_x, min_y, color='blue')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Minimization of 1D Function by Method of Newton')

plt.show()
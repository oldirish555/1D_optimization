import math as m 
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x+4)**2+2*x # example function

def golden_section(f, a, b, tol=1e-6):
    # Define the golden ratio
    phi = (1 + m.sqrt(5)) / 2
    
    # Initial interval
    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi
    fx1 = f(x1)
    fx2 = f(x2)
    
    # Iterative procedure
    while abs(b - a) > tol:
        if fx1 < fx2:
            b = x2
            x2 = x1
            fx2 = fx1
            x1 = b - (b - a) / phi
            fx1 = f(x1)
        else:
            a = x1
            x1 = x2
            fx1 = fx2
            x2 = a + (b - a) / phi
            fx2 = f(x2)
    
    # Return the midpoint of the final interval
    return (a + b) / 2


a = -10
b = 10
x = np.linspace(a, b, 100)
y = f(x)

min_x = golden_section(f, a, b, 0.01)
min_y = f(min_x)

plt.plot(x, y)
plt.scatter(a, f(a), color='green')
plt.scatter(b, f(b), color='red')
plt.scatter(min_x, min_y, color='blue')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Minimization of 1D Function by Golden Section Method')

plt.show()
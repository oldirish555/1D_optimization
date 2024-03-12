import math as m 
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x+4)**4 - 5*x**2 + 5 # example function

def ff(x):
    return 4*(x+4)**3 - 10*x # example function

def chords(f, ff, a, b, tol=1e-6):
    x = a - ff(a) / (ff(a) - ff(b)) * (a-b)
    # Iterative procedure
    while abs(ff(x)) > tol:
        if ff(x) > 0:
            b = x
        else:
            a = x
        x = a - ff(a) / (ff(a) - ff(b)) * (a -b)
    
    # Return the midpoint of the final interval
    return x


a = -10
b = 4
x = np.linspace(a, b, 100)
y = f(x)

min_x = chords(f, ff, a, b, 0.01)
min_y = f(min_x)

plt.plot(x, y)
plt.scatter(a, f(a), color='green')
plt.scatter(b, f(b), color='red')
plt.scatter(min_x, min_y, color='blue')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Minimization of 1D Function by Method of Chords')

plt.show()
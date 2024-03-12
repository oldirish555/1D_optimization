import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x+4)**2+2*x # example function

def razrad_search(f, a, b, eps):
    sh = (b-a)/4
    x0 = a
    fx0 = f(x0)
    while True:
        x1 = x0 + sh
        fx1 = f(x1)
        if fx0 > fx1:
            x0, fx0 = x1, fx1
            if x0 > a and x0 < b:
                xm = x0 + 0.5 * sh
                Fm = f(xm)
            if abs(sh) <= eps:
                break
            if Fm < fx0:
                x0, fx0 = xm, Fm
                sh *= 2
            else:
                sh /= 2
        else:
            sh = -sh
            x1, fx1 = x0, fx0

a = -10
b = 10
x = np.linspace(a, b, 100)
y = f(x)

min_x = razrad_search(f, a, b, 0.01)
min_y = f(min_x)

plt.plot(x, y)
plt.scatter(a, f(a), color='blue')
plt.scatter(b, f(b), color='blue')
plt.scatter(min_x, min_y, color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Minimization of 1D Function by Line Search Method')

plt.show()
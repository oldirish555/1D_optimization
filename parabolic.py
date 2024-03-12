import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x+4)**4+2*x**2 +5 # example function

def parabolic_minimization(f, a, b, c, tol=1e-6, max_iter=100):
    """Minimizes the function `f` using the method of parabolic approximation, given the initial points `a`, `b`, and `c`."""
    x_min = None
    iter_count = 0

    while iter_count < max_iter:
        iter_count += 1

        # Fit a parabola to the three points (a, fa), (b, fb), and (c, fc)
        fa = f(a)
        fb = f(b)
        fc = f(c)
        num = (b**2 - c**2)*fa + (c**2 - a**2)*fb + (a**2 - b**2)*fc
        denom = 2*((b - c)*fa + (c - a)*fb + (a - b)*fc)
        x_min = num / denom

        # Check if the minimum point is within the current interval [a, c]
        if x_min < a or x_min > c:
            x_min = (a + c) / 2

        # Check if the algorithm has converged to within the given tolerance
        if abs(x_min - b) < tol:
            break

        # Update the points a, b, and c based on the new minimum point x_min
        fx_min = f(x_min)
        if fx_min < fb:
            if x_min < b:
                c = b
            else:
                a = b
            b = x_min
        else:
            if x_min < b:
                a = x_min
            else:
                c = x_min

    return x_min

a = -10
b = -6
c = 3
x = np.linspace(a, c, 100)
y = f(x)

min_x = parabolic_minimization(f, a, b, 0.001)
min_y = f(min_x)

plt.plot(x, y)
plt.scatter(a, f(a), color='blue')
plt.scatter(c, f(c), color='blue')
plt.scatter(min_x, min_y, color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Minimization of 1D function by parabolic approximation')

plt.show()
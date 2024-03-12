import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x+4)**2+2*x # example function

def fibonacci_search(func, a, b, tol=1e-6):
    """Minimizes the function `func` on the interval [a, b] using the Fibonacci search method."""
    # Define the Fibonacci sequence up to the point where the interval is less than `tol`
    fib_seq = [1, 1]
    while (b - a) / fib_seq[-1] > tol:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])

    # Initial endpoints of the interval
    x1 = a + (b - a) * fib_seq[-3] / fib_seq[-1]
    x2 = a + (b - a) * fib_seq[-2] / fib_seq[-1]

    # Evaluate the function at the initial points
    f1 = func(x1)
    f2 = func(x2)

    # Perform the search
    for k in range(len(fib_seq) - 3, -1, -1):
        if f1 > f2:
            a, x1, f1 = x1, x2, f2
            x2 = a + (b - a) * fib_seq[k] / fib_seq[k+1]
            f2 = func(x2)
        else:
            b, x2, f2 = x2, x1, f1
            x1 = a + (b - a) * fib_seq[k-1] / fib_seq[k+1]
            f1 = func(x1)

    return (a + b) / 2  # Return the midpoint of the final interval as the minimum


a = -10
b = 10
x = np.linspace(a, b, 100)
y = f(x)

min_x = fibonacci_search(f, a, b, 0.001)
min_y = f(min_x)

plt.plot(x, y)
plt.scatter(a, f(a), color='blue')
plt.scatter(b, f(b), color='blue')
plt.scatter(min_x, min_y, color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Minimization of 1D Function by Fibonacci Method')

plt.show()
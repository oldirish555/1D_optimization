import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x+4)**4+2*x**2 +5 # example function

def fibonacci_search(f, a, b, epsilon):
    def fib(n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a
    
    n = 0
    while fib(n + 1) < (b - a) / epsilon:
        n += 1
        # print(n)   
    c = a + fib(n - 2) / fib(n) * (b - a)
    d = a + fib(n - 1) / fib(n) * (b - a)
    while n > 0:
        if f(c) < f(d):
            b = d
            d = c
            c = a + fib(n - 2) / fib(n) * (b - a)
            n -= 1
        else:
            a = c
            c = d
            d = a + fib(n - 1) / fib(n) * (b - a)
            n -= 1

    return (b + a) / 2

a = -10
b = 3
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
plt.title('Minimization of 1D function by parabolic approximation')

plt.show()
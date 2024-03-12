import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 3*np.sin(x) + 0.1*(x+2)**2 - 0.5*x # example function
    #return x**2 # example function
    

def ff(x):
    return 3*np.cos(x) + 0.2*(x + 1) - 0.5*x # minx = about 4.44

def method_for_l_search(a, b, deriv):  
    max_val = deriv(a)

    i = a
    while i < b:
        var = deriv(i)
        if max_val < var:
            max_val = var
        i += 0.01

    # print(b)
    #print(max_val)
    return max_val

def broken_line(f, a, b, L, tol=1e-6): # выполняет локальный поиск около первой точки пересечения прямых Липшица

    #L = method_for_l_search(a, b, ff)

    x_opt = 1 / (2 * L) * (f(a) - f(b) + L * (a + b)) # абсцисса точки пересечения прямых
    y_opt = 1 / 2 * (f(a) + f(b) + L * (a - b)) # ордината точки пересечения прямых
    p =     1 / 2 * (f(a) + f(b) + L * (a - b))

    delta = 1 / (2 * L) * (f(x_opt) - p)
    while 2 * L * delta > tol:
        x1 = x_opt - delta
        x2 = x_opt + delta

        if f(x1) < f(x2):
            x_opt = x1
        else:
            x_opt = x2

        p = (1 / 2) * (f(x_opt) + p)
        delta = 1 / (2 * L) * (f(x_opt) - p)
        print(x_opt, y_opt)    
    return x_opt



a = -7
b = 11
L = 5

x = np.linspace(a, b, 100)
y = f(x)

line_1 = -L*(x - a) + f(a)
line_2 = L*(x - b) + f(b)
xx = 1 / (2 * L) * (f(a) - f(b) + L * (a + b))
yy = L*(xx - b) + f(b)
y_opt = 1 / 2 * (f(a) + f(b) + L * (a - b))

line_3 = -L*(x - xx) + f(xx)
line_4 = L*(x - xx) + f(xx)
# xxx = 0.5*((f(a) - f(b))/L) +b +a
# yyy = L*(xx - b) + f(b)


min_x = broken_line(f, a, b, L, 0.01)
min_y = f(min_x)

plt.plot(x, y)
plt.plot(a, f(a), 'ro')
plt.axvline(x=a, linewidth=1, color='r', linestyle='dashed')
plt.plot(b, f(b), 'ro')
plt.axvline(x=b, linewidth=1, color='r', linestyle='dashed')
plt.scatter(min_x, min_y, color='cyan')

# plt.plot(x,line_1, linewidth=0.5, color='green', linestyle='dashed')
# plt.plot(x,line_2, linewidth=0.5, color='green', linestyle='dashed')
# plt.scatter(xx, f(xx), color='blue')
# plt.plot(xx, y_opt, 'go')

# plt.plot(x,line_3, linewidth=0.5, color='green', linestyle='dashed')
# plt.plot(x,line_4, linewidth=0.5, color='green', linestyle='dashed')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Minimization of 1D Function by Broken Line Method')

plt.show()
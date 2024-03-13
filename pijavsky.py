import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -10*np.cos(x) + 0.2*(x-2)**2   # Example function


# implementation of Pijavsky Optimization
def pijavsky_optimize(a, b, n, eps, L, f):
    #u = np.zeros(n+2) #верхние вершины ломаной линии
    u = list()
    #uy = np.zeros(n+2) 
    v = np.zeros(n+1) #нижние вершины ломаной линии
    v = list()
# нулевая итерация
    # u[0] = a
    # u[1] = b
    u.append(a)
    u.append(b)

    
    line_1 = -L*(x - a) + f(a)
    line_2 = L*(x - b) + f(b)
    
    # v[0] = 1 / (2 * L) * (f(a) - f(b) + L * (a + b))
    v.append(1 / (2 * L) * (f(a) - f(b) + L * (a + b)))

    y0 = 1 / 2 * (f(a) + f(b) + L*(a - b))
    
    plt.plot(x,line_1, linewidth=0.5, color='green', linestyle='dashed')
    plt.plot(x,line_2, linewidth=0.5, color='green', linestyle='dashed')
    plt.plot(v[0], f(v[0]), 'bv')
    plt.plot(v[0], y0, 'b^')
    
    for k in range(2, n+2):
        v_min = v[k - 2]  # поиск абсциссы минимальной точки всего массива v
        # if abs(f(v_min) - v_min):
        #     u_min = u[k]      
        #     break
        u[k] = v_min
        # добавить u[k] в список U
        # удалить v_min  из списка V
        vkl = 1/(2*L) * (f(u[k-1])-f(u[k])) + 0.5* (u[k-1] +u[k])
        vkr = 1/(2*L) * (f(u[k])-f(u[k+1])) + 0.5* (u[k+1] +u[k])
        # добавить vkl и vkr в список V
        
    return -4

a = -8
b = 7.7
x = np.linspace(a, b, 100)
y = f(x)

n = 1
L = 16 # Lipschitz constant
e = 0.01

min_x = pijavsky_optimize(a, b, n, e, L, f)


min_y = f(min_x)
plt.plot(x, y)
plt.scatter(a, f(a), color='red')
plt.axvline(a, 0, 1, color="red", linestyle="dashed")
plt.scatter(b, f(b), color='red')
plt.axvline(b, 0, 1, color="red", linestyle="dashed")
plt.scatter(min_x, min_y, color='blue')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Minimization of 1D Function by Broken Line Method')

plt.show()
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Valores dados
x_valores = np.array([2, 3, 5, 7, 8], dtype=float)
fx = np.array([6, 19, 99, 291, 444], dtype=float)  # f(x) actualizados

n = len(x_valores)
b = np.copy(fx)

# 1) Cálculo de coeficientes
for k in range(1, n):
    b[k:n] = (b[k:n] - b[k-1]) / (x_valores[k:n] - x_valores[k-1])

# 2) Construcción del polinomio
x = sp.Symbol('x')
polinomio_newton = b[0]
for j in range(1, n):
    termino = 1
    for i in range(j):
        termino *= (x - x_valores[i])
    polinomio_newton += b[j] * termino

# Mostrar el polinomio
print("Polinomio de interpolación de Newton:")
print(sp.expand(polinomio_newton))

# Convertir el polinomio simbólico a función numérica
polinomio_newton_fun = sp.lambdify(x, polinomio_newton, 'numpy')

# Gráfica
eje_x = np.linspace(min(x_valores), max(x_valores), 200)
eje_y = polinomio_newton_fun(eje_x)

plt.plot(eje_x, eje_y, label='Polinomio de Newton')
plt.plot(x_valores, fx, 'o', label='Datos originales')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación de Newton')
plt.grid(True)
plt.legend()
plt.show()
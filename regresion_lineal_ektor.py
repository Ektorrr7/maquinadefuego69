import numpy as np
import matplotlib.pyplot as plt

# Datos dados
X = np.array([1, 2, 3, 4, 5, 6], dtype=float)
Y = np.array([5.04, 8.12, 10.64, 13.18, 16.20, 20.04], dtype=float)

# Cálculos para regresión lineal
n = len(X)
sum_xiyi = sum(X * Y)
sum_xi2 = sum(X ** 2)

a1 = (n * sum_xiyi - sum(X) * sum(Y)) / (n * sum_xi2 - sum(X) ** 2)
a0 = (sum(Y) / n) - a1 * (sum(X) / n)

# Función de regresión
y_regresion = lambda x: a0 + a1 * x

# Imprimir estimaciones para algunos valores
datos_estimar = [1, 3.5, 6]
for dato in datos_estimar:
    print(f'Años {dato}: salario estimado: {y_regresion(dato):.2f}')

# Imprimir ecuación
print(f'\nLa función de regresión es: y = {a1:.4f}x + {a0:.4f}')

# Graficar
x_grafica = np.linspace(min(X), max(X), 100)
y_grafica = y_regresion(x_grafica)

plt.plot(x_grafica, y_grafica, label='Línea de regresión')
plt.plot(X, Y, 'o', label='Datos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regresión Lineal')
plt.grid(True)
plt.legend()
plt.show()
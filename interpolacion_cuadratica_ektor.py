import numpy as np
import matplotlib.pyplot as plt

# Puntos originales
xi = np.array([1, 2, 3, 5, 7, 8])
fi = np.array([3, 6, 19, 99, 291, 444])

# Tomamos 3 puntos cercanos a x = 4 para interpolación cuadrática
x_interp = np.array([2, 3, 5], dtype=float)
f_interp = np.array([6, 19, 99], dtype=float)

# Función de interpolación cuadrática de Lagrange
def lagrange_quad(x, x_vals, y_vals):
    total = 0
    for i in range(3):
        term = y_vals[i]
        for j in range(3):
            if j != i:
                term *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
        total += term
    return total

# Estimar f(4)
x_estimar = 4
f4 = lagrange_quad(x_estimar, x_interp, f_interp)
print(f"El valor estimado de f({x_estimar}) con interpolación cuadrática es: {f4:.2f}")

# Generar puntos para graficar la curva
x_vals = np.linspace(2, 5, 200)
y_vals = [lagrange_quad(x, x_interp, f_interp) for x in x_vals]

# Graficar puntos originales y la curva interpolada
plt.plot(xi, fi, 'o', label='Datos originales')
plt.plot(x_vals, y_vals, 'g-', label='Interpolación cuadrática')
plt.plot(x_estimar, f4, 'ks', label=f'Estimación f({x_estimar}) = {f4:.2f}')
plt.title("Interpolación cuadrática (Lagrange)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
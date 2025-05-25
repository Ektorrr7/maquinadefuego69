import numpy as np
import matplotlib.pyplot as plt

# Datos conocidos
xi = np.array([1, 2, 3, 5, 7, 8])
fi = np.array([3, 6, 19, 99, 291, 444])

# Puntos para interpolar
x0, x1 = 3, 5
f0, f1 = 19, 99
x = 4

# Interpolación lineal
f_interp = f0 + ((f1 - f0) / (x1 - x0)) * (x - x0)
print(f'El valor estimado de f({x}) por interpolación lineal es: {f_interp:.2f}')

# Graficar los puntos y la línea de interpolación
plt.plot(xi, fi, 'o', label='Datos conocidos')
plt.plot([x0, x1], [f0, f1], 'r--', label='Segmento de interpolación')
plt.plot(x, f_interp, 'ks', label=f'Estimación f({x}) = {f_interp:.2f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación lineal entre f(3) y f(5)')
plt.grid(True)
plt.legend()
plt.show()
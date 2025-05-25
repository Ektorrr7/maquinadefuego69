import numpy as np
import math
from scipy.integrate import quad

# ----------- FUNCIONES PARA INTEGRAR -----------

def f1(x): return 2 * np.cos(2 * x)
def f2(x): return -x**2 - x/2 + 4
def f3(x): return np.exp(-x**2)

# ----------- INTEGRACIÓN ANALÍTICA -----------

def analitica_f1(): return quad(f1, 0, np.pi/4)[0]
def analitica_f2(): return quad(f2, 0.5, 1.5)[0]
def analitica_f3(): return quad(f3, 0, 1)[0]

# ----------- MÉTODOS NUMÉRICOS DE INTEGRACIÓN -----------

def trapecio_simple(f, a, b):
    return (b - a) * (f(a) + f(b)) / 2

def trapecio_multiple(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return h * (y[0] + 2 * sum(y[1:-1]) + y[-1]) / 2

def simpson_1_3(f, a, b):
    m = (a + b) / 2
    return (b - a) / 6 * (f(a) + 4*f(m) + f(b))

def simpson_3_8(f, a, b):
    h = (b - a) / 3
    return 3*h/8 * (f(a) + 3*f(a + h) + 3*f(a + 2*h) + f(b))

# ----------- FUNCIONES PARA DERIVAR -----------

def f_derivada(x): return -2*x - 0.5  # derivada analítica

def derivada_adelante(f, xi, h):
    return (-f(xi + 2*h) + 4*f(xi + h) - 3*f(xi)) / (2*h)

def derivada_atras(f, xi, h):
    return (3*f(xi) - 4*f(xi - h) + f(xi - 2*h)) / (2*h)

def derivada_centrada(f, xi, h):
    return (-f(xi + 2*h) + 8*f(xi + h) - 8*f(xi - h) + f(xi - 2*h)) / (12*h)

def error_relativo(exacto, aprox):
    return abs((exacto - aprox) / exacto) * 100

# ----------- EJECUCIÓN DE CÁLCULOS -----------

print("\n---- INTEGRACIÓN ----")
print("Integral f1 (2cos(2x)) en [0, π/4]:")
print("Analítica:", analitica_f1())
print("Trapecio simple:", trapecio_simple(f1, 0, np.pi/4))
for n in [2, 4, 6]:
    print(f"Trapecio múltiple n={n}:", trapecio_multiple(f1, 0, np.pi/4, n))
print("Simpson 1/3:", simpson_1_3(f1, 0, np.pi/4))
print("Simpson 3/8:", simpson_3_8(f1, 0, np.pi/4))

print("\nIntegral f2 (-x² - x/2 + 4) en [0.5, 1.5]:")
print("Analítica:", analitica_f2())
print("Trapecio simple:", trapecio_simple(f2, 0.5, 1.5))
for n in [2, 4, 6]:
    print(f"Trapecio múltiple n={n}:", trapecio_multiple(f2, 0.5, 1.5, n))
print("Simpson 1/3:", simpson_1_3(f2, 0.5, 1.5))
print("Simpson 3/8:", simpson_3_8(f2, 0.5, 1.5))

print("\nIntegral f3 (e^(-x²)) en [0,1]:")
print("Analítica (aprox):", analitica_f3())
print("Trapecio simple:", trapecio_simple(f3, 0, 1))
for n in [2, 4, 6]:
    print(f"Trapecio múltiple n={n}:", trapecio_multiple(f3, 0, 1, n))
print("Simpson 1/3:", simpson_1_3(f3, 0, 1))
print("Simpson 3/8:", simpson_3_8(f3, 0, 1))

# ----------- DERIVACIÓN NUMÉRICA -----------

xi = 0
for h in [0.2, 0.1]:
    print(f"\n---- DERIVACIÓN EN x={xi} con h={h} ----")
    exacta = f_derivada(xi)
    adelante = derivada_adelante(f2, xi, h)
    atras = derivada_atras(f2, xi, h)
    centrada = derivada_centrada(f2, xi, h)

    print(f"Derivada exacta: {exacta}")
    print(f"Adelante (O(h²)): {adelante}, Error: {error_relativo(exacta, adelante):.4f}%")
    print(f"Atrás (O(h²)): {atras}, Error: {error_relativo(exacta, atras):.4f}%")
    print(f"Centrada (O(h⁴)): {centrada}, Error: {error_relativo(exacta, centrada):.4f}%")


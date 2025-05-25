

import numpy as np
import matplotlib.pyplot as plt

def multiplos_fila(x):
  multiplos = np.zeros((x,x))

  if x>=0 and x%1==0:
    aleatorio = np.random.randint(1,10,x)
    for i in range(x):
      fila = (i+1)*aleatorio
      multiplos[i,:] = fila
  else:
    print(x, 'no es un numero entero ni positivo')
  return multiplos

def multiplos_columna(x):
  multiplos = np.zeros((x,x))

  if x>=0 and x%1==0:
    aleatorio = np.random.randint(1,10,x)
    for i in range(x):
      columna = (i+1)*aleatorio
      multiplos[:,i] = columna
  else:
    print(x, 'no es un numero entero ni positivo')
  return multiplos

M = multiplos_fila(6)
N = multiplos_columna(6)
print('M = ', M , '\n')
print('N = ', N , '\n')

#Inciso 6).
#Intervalo y numero de muetras para x
x = np.linspace(-2*np.pi, 2*np.pi, 100)

#Funciones
y1 = x**2        #Polinomio
y2 = np.sin(x)   #Función trigonométrica
y3 = np.exp(-x)  #Función exponencial

#Crear la gráfica
plt.plot(x, y1, 'r--', label='f(x) = x^2')     # Línea roja con línea discontinua
plt.plot(x, y2, 'g-.', label='f(x) = sin(x)')  # Línea verde con línea punto y guion
plt.plot(x, y3, 'b:', label='f(x) = exp(-x)')  # Línea azul con línea punteada

#Título y etiquetas
plt.title('Gráfica de Tres Funciones')
plt.xlabel('x')
plt.ylabel('f(x)')

#Mostrar la cuadrícula
plt.grid(True)

#Agregar la leyenda
plt.legend()

#Mostrar la gráfica
plt.show()

import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: x**3 - 5*x**2 + 5*x - 1

raiz_1 = lambda a, b, c: (-b+np.sqrt(b**2-4*a*c))/(2*a)
raiz_2 = lambda a, b, c: (-b-np.sqrt(b**2-4*a*c))/(2*a)

a = np.array([1,-5,5,-1]) # La doble [[]] es por las filas y columnas, es bidimensional.
xi = 0.8

b = np.empty(len(a)) #empty es para mas rapidez
c = np.empty(len(a))
#print(b)
num_iteraciones = 10
n = len(a)

#Division sintetica.
for i in range(1,num_iteraciones + 1): #Hace las iteraciones
    for j in range(n): #recorre los vectores (div, sintetica)
        if j==0:
            b[j] = a[j]
            c[j] = a[j]
        else:
            b[j] = a[j]+xi*b[j-1]
            c[j] = b[j]+xi*c[j-1]
        xi_viejo = xi
    xi = round(xi_viejo - (b[n-1]/c[n-2]),5)
    print(f'Iteracion: {i} ')
    print(f'xi = {xi_viejo} ')
    print(b)
    print(c)
    print('\n')
    if i == num_iteraciones:
        raiz1 = round(raiz_1(b[0],b[1],b[2]),5)
        raiz2 = round(raiz_2(b[0],b[1],b[2]),5)
        print(f'Raices: x1= {raiz1} y x2= {raiz2}')
        print('\n')

x = np.linspace(-1,3,1000)
plt.plot(x,fx(x))
plt.plot(xi,fx(xi),'ro') #son las coordenadas.
plt.grid()
plt.show()


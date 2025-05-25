import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: 8*x*np.sin(x)*np.exp(-x)-1
error_rel = lambda va, vn: (np.abs(va - vn)/np.abs(va))*100
xviejo = -0.3
xnuevo = 0.5

num_iteraciones = 5

for i in range(num_iteraciones):
  xi = round(xviejo-(fx(xviejo))*(xnuevo-xviejo)/(fx(xnuevo)-fx(xviejo)),4)
  er = round(error_rel(xi,xviejo),4)
  xnuevo = xviejo
  xviejo = xi
  print('..........................................................')
  print(f'i = {i+1} | xi = {xviejo} | x_0 = {xnuevo} | er = {er} %')

x = np.linspace(-5,5,100)
plt.plot(x,fx(x))
plt.plot(xi,fx(xi),'ro')
plt.grid()
plt.show()


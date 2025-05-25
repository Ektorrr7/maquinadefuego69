import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: 2*x*np.cos(2*x)-(x+1)**2
error_rel = lambda vn, va: (np.abs(va - vn)/np.abs(vn))*100
xr = -2.1913
a = -3
b = -2

xi = round((a+b)/2,4)
num_iteraciones = 5

for i in range(num_iteraciones):
  aviejo = a
  bviejo = b
  xi = (a+b)/2
  fa = fx(a)
  fb = fx(b)
  fxi = fx(xi)
  er = round(error_rel(xr,xi),4) #round limita los decimales?

  if fa*fxi < 0:
    b = xi
  else:
    a = xi
  print('..........................................................')
  print(f'i = {i+1} | a = {aviejo} | b = {bviejo} | xi = {xi} | er = {er} %')

x = np.linspace(-5,5,100)
plt.plot(x,fx(x))
plt.plot(xi,fx(xi),'ro') #son las coordenadas.
plt.grid()
plt.show()


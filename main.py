import numpy as np
import pylab as pl
# crea un vector(arreglo) con los valores del eje x
x=[1,2,3,4,5]
# crea un vector (arreglo) con los valores del eje y 
y=[1,4,9,16,25]
#grafica el vector x contra el vector y 
pl.plot(x,y)
# guarda la imagen
pl.savefig('temp1.png')


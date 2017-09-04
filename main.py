import numpy as np
import pylab as pl
# crea un vector(arreglo) con los valores del eje x
x=[1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
# titulo del eje
pl.ylabel('numero de novias+mascotas')
# crea un vector (arreglo) con los valores del eje y 
y=[0,0,1,2,2,2,2,1,4,5,5,5,6,7,7,7,7,7,6,4,7,7]
#titulo del eje
pl.xlabel('anios')
#grafica el vector x contra el vector y 
pl.plot(x,y)
pl.plot(x,y,'ro')
# guarda la imagen
pl.savefig('temp1.png')


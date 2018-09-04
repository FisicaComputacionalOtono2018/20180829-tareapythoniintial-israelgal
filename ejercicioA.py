import numpy as np
import math
import matplotlib.pyplot as plt 
def f1(x):
	return (2*np.sqr(x))+(5*x)-2
def f2(x):
	return 4*x+1
x1 = np.arange(-10, 15, 0.1)	
x2 = np.arange(-10, 15, 0.2)

plt.plot(x1, f1(x1), 'bo' , x2, f2(x2), 'k')

plt.savefig('Ejercicio A.png')

plt.show
# Write a suitabe program to plot Legendary Polinomial for n=6 within the interval x=-1.0 to +1.0 and y=-1.0 to +1.0
# This program is witten by Sk Salman Parbhage
#Editor: Sublime text 3 || Python 3.6.9 || Numpy: 1.18.0 || Matplotlib: 3.1.2 ||Scipy: 3.1.2
from scipy.special import legendre
import matplotlib.pyplot as plt 
import numpy as np 
min = -1.0
max = 1.0
step = 0.001
for n in range(6):
	pn = legendre(n)
	x = np.arange(min, max+step, step)
	y = pn(x)
	plt.plot(x,y, linewidth=1, linestyle="-", )
plt.legend(('$\mathcal{P}_0(x)$', '$\mathcal{P}_1(x)$', '$\mathcal{P}_2(x)$', '$\mathcal{P}_3(x)$', '$\mathcal{P}_4(x)$', '$\mathcal{P}_5(x)$'), loc = "lower right")
plt.xlabel('$x$')
plt.ylabel('$\mathcal{j}_n(x)$')
plt.xlim(-1.0,1.0)
plt.ylim(-1.0,1.01)
plt.grid('true')
plt.title("Legendary Polinomial")
plt.show()
import numpy as np
import pylab as py
import scipy.special as sp

x = np.linspace(0,15,500000)

for v in range(0,6):
	py.plot(x, sp.jv(v,x))
py.xlim((0,15))
py.ylim((-0.5, 1.1))
py.legend(('$\mathcal{j}_0(x)$', '$\mathcal{j}_1(x)$', '$\mathcal{j}_2(x)$', '$\mathcal{j}_3(x)$', '$\mathcal{j}_4(x)$', '$\mathcal{j}_5(x)$'), loc = 0)
py.xlabel('$x$')
py.ylabel('$\mathcal{j}_n(x)$')
py.title("Bessel Plot")
py.grid(True)
py.show()
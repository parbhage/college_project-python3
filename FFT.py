import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [16, 12]
plt.rcParams.update({'font.size':18})
# create a simple signal with two frequencies
dt = 0.001
t = np.arange(0,1,dt)
f = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*120*t) #sum of two frequencies
f_clean = f
f = f+ 2.5*np.random.randn(len(t))      #adding some noise

plt.plot(t, f, color='c',lineWidth=1.0, label= 'Noisy')
plt.plot(t,f_clean, color= 'k', LineWidth=1.5, label='Clean')
plt.xlim(t[0],t[-1])
plt.legend()
plt.show()

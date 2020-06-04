# Read the random 20 data plot force vs displacement curve of the Spring Constant of Hook's Law.Obtain the strigth line fit and find the spring constant.
# This program is witten by Sk Salman Parbhage
#Editor: Sublime text 3 || Python 3.6.9 || Numpy: 1.18.0 || Matplotlib: 3.1.2
import matplotlib.pyplot as plt
import numpy as np 
#ganerate the random smple data
N = 20
k_theoretical = 3
displacement =np.arange(N)
force = k_theoretical * displacement + np.random.normal(size=N)
#Calculate constant for Hook's law
avgF = force.mean()
avgX = displacement.mean()
k_calculated = avgF / avgX
#Plot data points and line
plt.plot(displacement, force, "bx")
plt.plot(displacement, k_calculated * displacement, "r-" , label = "k = {:.2f}".format(k_calculated))
plt.xlabel("Displacement")
plt.ylabel("Force")
plt.title("Spring constant of Hook's Law")
plt.legend()
plt.show()


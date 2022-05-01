#NCERT Class 10; Ex-15.1, Q-23
#Varshini Jonnala
#CS21BTECH11024

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Creating PMF of Binomial Random Variable X = {0,1,2,3}
#X denoting number of heads in the trails of tossing a coin 3 times

xk = np.arange(0,4)
pk = (1/8,3/8,3/8,1/8)
custm = stats.rv_discrete(name='custm', values=(xk, pk))

#plotting PMF
fig, ax = plt.subplots(1, 1)
ax.plot(xk, custm.pmf(xk), 'ro', ms=8, mec='b')
ax.vlines(xk, 0, custm.pmf(xk), colors='blue', linestyles='--', lw=2)

plt.title('PMF',fontsize = 18)
plt.xlabel('Value of X',fontsize = 15)
plt.ylabel('Probability',fontsize = 15)

plt.grid()
plt.show()

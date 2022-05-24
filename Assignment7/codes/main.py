#Papoulis; Ex-3.12
#Varshini Jonnala
#CS21BTECH11024

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Creating PMF of Binomial Random Variable X = {0,1,2,3}
#X denoting the number of times the chosen number 'k' appears on the 3 dice.
xk = np.arange(0,4)
pk = (125/216,75/216,15/216,1/216)
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

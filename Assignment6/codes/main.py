#NCERT Class 12; Ex-13.4, Q-17
#Varshini Jonnala
#CS21BTECH11024

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Creating PMF of Binomial Random Variable X = {0,1,2}
#X denoting number of aces when two cards are randomly drawn from deck of cards
xk = np.arange(0,3)
pk = (1128/1326,192/1326,6/1326)
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

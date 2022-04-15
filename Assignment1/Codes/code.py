import numpy as np
from matplotlib import pyplot as plt

A = np.array(([2,5]))
B = np.array(([-1,2]))

#M divides AB line segment in 1:2 ratio :
G = 2*A + B

M = np.array(G/(1+2))
print("M", M)

C = np.array(([5,8]))
M = np.array(([1,4])) 
#finding coefficients of x and y and constant
a = C[1] - M[1]
b = M[0] - C[0]
c = a*(C[0]) + b*(C[1])
   
print("The line passing through points C and M is:",a,"x",b,"y =",c, "\n")

#A(2,5)
#B(-1,2)
#C(5,8)
#M(1,4)
data = np.array([
    [2,5],
    [-1,2],
    [5, 8],
    [1,4]
])
x, y = data.T
plt.plot(x,y, marker = 'o')

plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")

plt.annotate('A(2,5)',(2,5),(2.2,5))
plt.annotate('B(-1,2)',(-1,2),(-0.7,2))
plt.annotate('M(1,4)',(1,4),(1.2,4))
plt.annotate('C (5,8)',(5,8),(4.3,8))

plt.title('Plotting of the points A,B,C, and M')
plt.grid()
plt.show()

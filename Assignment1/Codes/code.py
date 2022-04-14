import numpy as np
from matplotlib import pyplot as plt

import matplotlib.pyplot as plt

def section(m,n,x1,y1,x2,y2) : 
  #function to find the point that divides the line segment joining (x1,y1),(x2,y2) in m:n ratio.
  #Section formula
  x = (float) (m * x2 + n * x1)/(m+n)
  y = (float) (m * y2 + n * y1 )/(m+n)
  print("M (",x,",",y,")")

m,n = 1,2
x1,y1 = 2,5
x2,y2 = -1,2
section(1,2,2,5,-1,2) 

def line(C, M):
 
    a = C[1] - M[1]
    b = M[0] - C[0]
    c = -a*(C[0]) - b*(C[1])
 
    if(b > 0):
        print("The line passing through points C and M is:",
              a, "x + ", b, "y +",c,"= 0", "\n")
    else:
        print("The line passing through points C and M is: ",
              a, "x", b,"y +",c,"= 0", "\n")

C = [5, 8]
M = [1, 4]
line(C, M)

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

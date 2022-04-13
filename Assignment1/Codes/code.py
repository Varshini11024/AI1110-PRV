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
plt.plot([2,-1,5,1,2],[5,2,8,4,5],marker = 'o')
plt.annotate('A(2,5)',(2,5),(2.5,5),arrowprops={"arrowstyle":"<-"})
plt.annotate('B(-1,2)',(-1,2),(-0.5,2),arrowprops={"arrowstyle":"<-"})
plt.annotate('M(1,4)',(1,4),(1.5,4),arrowprops={"arrowstyle":"<-"})
plt.annotate('C (5,8)',(5,8),(4,8),arrowprops={"arrowstyle":"<-"})

plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")

plt.title('Graph of x-y+3=0 or 4x-4y+12=0')
plt.grid()
plt.show()

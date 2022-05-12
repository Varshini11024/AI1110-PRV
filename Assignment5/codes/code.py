import random
import numpy as np
import math

def nCr(n,r):
    f = math.factorial
    return f(n)/(f(r)*f(n-r))

#Total no.of lottery tickets sold is 10,000
N = 10000
#The number of tickets that are not awarded any prize in the lottery is N-10 = 9990
M = 9990

print("The Probability of not getting a prize if bought 1 ticket is", nCr(M,1)/nCr(N,1))
print("The Probability of not getting a prize if bought 2 tickets is", round(nCr(M,2)/nCr(N,2), 5))
print("The Probability of not getting a prize if bought 10 tickets is", round(nCr(M,10)/nCr(N,10), 5))

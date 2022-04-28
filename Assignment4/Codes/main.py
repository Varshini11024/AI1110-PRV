import numpy as np
from numpy import random as RN 

#Total number of outcomes possible when a coin was tossed 3 times
N = 8

#Number of favourable outcomes of Hanif winning the game
#Hanif wins on getting 3Heads or 3Tails on tossing the coin 3 times
n_1 = 2
n_0 = N - n_1

#The Theoretical probabilities
pr_0 = n_0/N
pr_1 = n_1/N
print("The Probability that Hanif will lose the game is ", pr_0)
print("The Probability that Hanif will win the game is ", pr_1)

#Generating samples
T = np.random.choice([0, 1], size=(N))

#obtaining frequencies and probabilities
X0 = np.count_nonzero(T == 0)
X1 = np.count_nonzero(T == 1)
P0 = X0/N
P1 = X1/N

#The empirical probabilities
print('n(X=0) = ', X0)
print('n(X=1) = ', X1)
print('Pr(X=0) = ', P0)
print('Pr(X=1) = ', P1

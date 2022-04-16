#P(A) = 1/2
#P(B) = 1/3
p_a = 1/2
p_b = 1/3
p_a_intersec_b = 1/4

#finding P(A|B) and P(B|A)
p_a_given_b = (p_a_intersec_b)/p_b
print('P(A|B) =', p_a_given_b)
 
p_b_given_a = (p_a_intersec_b)/p_a
print('P(B|A) =', p_b_given_a)

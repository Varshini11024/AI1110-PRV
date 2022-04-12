def calc(p_a, p_b, p_a_intersec_b):

 p_a_given_b = (p_a_intersec_b)/p_b
 print('P(A|B) =', p_a_given_b)

 p_b_given_a = (p_a_intersec_b)/p_a
 print('P(B|A) =', p_b_given_a)


#P(A) = 1/2
#P(B) = 1/3
#p_a_intersec_b = 1/4
#finding P(A|B) and P(B|A)

calc(1/2, 1/3, 1/4)

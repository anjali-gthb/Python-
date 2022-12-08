# print(2+3*6)
# print(2/4)
# print(4/2) #floating point division.
# print(5//6) #integer division.
# power
# print(2**3) #2^3;
# print(2**0.5)
# print(round(2**0.5,3));

# associativity and precedence
print(2**3/2*6-4*(3-4/2))
# 1st priority-->bracket
# (3-4/2) now b/w (/ and -) choose / (divide becoz it has high precedence)

# (2**3/2*6-4*1)
# now **(exponent has higher precedence)

# (8/2*6-4*1)
# since / and * has the same precedence therefore now we move to associativity
# and associativity is left to right

# 4*6-4*1--> 24-4*1-->24-4-->20
print(2**2**3)

# Bitwise Operations in Python:-
# => Bitwise operations are used to perform operations on binary numbers.
# => it works on bits and performs bit by bit operation.

# EX: &, |, ^, ~, 

# AND(&) Operator:-
# It returns 1 if both the bits are 1. 

a = 10
b = 4
x = 5
y = 3
print(a & b)  # 0
print(x & y) # 1

print( 5 & 6)



# Binary Table:-
# 0000 = 0
# 0001 = 1
# 0010 = 2
# 0011 = 3
# 0100 = 4
# 0101 = 5
# 0110 = 6
# 0111 = 7
# 1000 = 8
# 1001 = 9
# 1010 = 10 => A
# 1011 = 11 => B
# 1100 = 12 => C
# 1101 = 13 => D
# 1110 = 14 => E
# 1111 = 15 => F




# AND(&) Operator:-
# It returns 1 if both the bits are 1.


# 1 => True
# 0 => False

    
 
#   4  4
# +3  3
# —--------
#   7  7



a = 10
b = 4
print(a & b) 

# => Binary number of a => 1010
# => binary number of b => 0100


#     1  0  1  0
# &  0  1  0  0
# —-----------------
#     0  0  0   0    => 0



x = 5
y = 3
print(x & y)

# => binary of 5 => 0101
# => binary of 3 => 0011

#      0 1 0 1
# &   0 0 1 1
# —---------------
#      0 0 0 1     =>1

# 1 & 1 => 1,0 & 1 => 0,1 & 0 => 0,0 & 0 => 0


# => binary number of 5 => 0101
# => binary number of 6 => 0110

#       0 1 0 1
#  &   0 1 1 0
# —---------------
#       0 1 0 0     => 4

#  1 & 0 => 0, 0 & 1 => 0, 1 & 1 => 1, 0 & 0 => 0



# Bitwise Or oprator
A = 5
B = 6
print(A | B)


#5 = 0101
#6 = 0110
   # 0111

A = 50 
B = 6
print(A ^ B)

#5 = 0101
#6 = 0110
   # 0011



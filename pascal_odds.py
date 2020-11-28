# represent with binary string for 1=odd, 0=even (don't need actual number)
# next row is b xor (b << 1)

# 1
# 1 1
# 1 2 1
# 1 3
# etc.

# def popcount(x):
#     x -= (x >> 1) & 0x5555555555555555 # flr(x/2) + x & 1
#     x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
#     x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
#     return ((x * 0x0101010101010101) & 0xffffffffffffffff ) >> 56

# print(popcount(0x111))


#  1101011011
#  abcdefghij
# -0a0c0e0g0i
# =0a0c0e0g0i
# +0b0d0f0h0j

#  ab00ef00ij
# +0000cd00gh

#  ab0000ghij
# +000000cdef

#  

#     0abcdefghij
# xor abcdefghij0

# 

# 011010110
# 011010111

# 000010011
# 000110001

def num_ones(b):
    n = 0
    while b:
        n += b&1
        b = b >> 1
    return n


b = 1
odds = [1]
print("{0:b}".format(b))
for i in range(1000):
    b = b ^ (b << 1)
    # print("{0:b}".format(b))
    odds.append(num_ones(b))

# print(odds)

row_nums = list(range(1,len(odds)+1))
# 00 -> 0
# 01 -> 1
# 10 -> 1
# 11 -> 0

# print(sum(row_nums), sum(odds), sum(odds)/sum(row_nums), 0.75**(len(row_nums)-1))

# import math
# def area(n): # portion given number of rows
#     return math.pow(0.75, n.bit_length() - 1


# just cellular automata generating pascal's triangle!!
# percent odd = shaded portion of pascal triangle

# at each iteration, pascal removes 1/4 of area.
# area = 3/4^logn ---> approaches 0! almost no odd numbers in pascal!

# alittle wonky, since we have a full row of ones. OBOE.
# triangles length --> 0, 1, 3, 7, ... 2^k - 1
# separated by 1's
# 2^k-long pascal
#   2^k = 1 + 2^0-1 + 1 + 2^1-1 + ... + 2^(k-1)-1 + 1
#       = 1 + 2^0       + 2^1   + ... + 2^(k-1)
# 1  2^k-1
# 3^(k-1 - i) appearances of 2^i-1 triangle
# area of 2^i-1 is a(a+1)/2 = (2^i-1)2^(i-1) = 2^(2i-1) - 2^(i-1)
#  sum over i from 0 to k-1:   3^(k-1 - i) 2^(i-1) (2^i - 1)
# /sum over i from 1 to 2^k:   i

# 
# 2^(k-1)(2^k + 1)

# 1
# 11
# 101
# 1111

# 2^k-long. 2^(k-1)-1 long triangle
# (2^(k-1)-1)*2^(k-2)  /  2^(k-1)*(2^k+1)
#  = (2^(k-1)-1)/(2*(2^k+1))
#  = 2^(k-2)/(2^k+1) - 1/(2*(2^k+1))
#  < 1/4 - 0

# 1/4 - 2^(k-1)/(2^(k-1)*(2^k+1))  # same as normal, minus 1 row out of the total area
# 1/4 - 1/(2^k + 1)
# (2^k + 1)/(4(2^k + 1)) - 4/4*(2^k + 1)
# (2^k - 3)/(4(2^k + 1))
# 2^(k-2)/(2^k + 1) - 3/4*(2^k + 1)

# tri_size*4 + 2^k + 2^(k-1) = tot_size
# tri_size*4 = tot_size - 3* 2^(k-1)
# tri_size/tot_size = 1/4 - 3/4 * 2^(k-1) / tot_size
# 1 - ratio = 3/4 (1 + 2^(k-1)/(2^(k-1) * (2^k + 1))
#           = 3/4 (1 + 1/(2^k + 1))

# area = tot_area * biggest_tri_ratio * next_tri_ratio * ... * smallest_tri_ratio
# area/tot_area = prod_i=1^k  3/4 (1 + 1/(2^i + 1))
#               = prod_i=1^k  3/2 (2^(i-1) + 1)/(2^i + 1)
#               = (3/2)^k * 2/(2^k + 1)
#               = 3^k / (n*(n+1)/2)

# look at the 1's!!! each doubling of length, the number of ones triples.
# ones = 3^k
# tot  = n*(n+1)/2
import math
def area(n): # portion given number of rows
    return math.pow(3, n.bit_length() - 1) / (n * (n + 1) / 2)

ones = tot = 0
for i in range(len(odds)):
    ones += odds[i]
    tot += row_nums[i]
    if num_ones(row_nums[i]) == 1:
        print(f"{row_nums[i]} guess: {area(row_nums[i])}, measured: {ones/tot}")


# import matplotlib.pyplot as plt 

# plt.scatter(row_nums, odds)
# plt.show()
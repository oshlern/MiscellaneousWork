import numpy as np
import math
import sympy

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    # print("inv", a, b, x1)
    return x1

def discrete_log(c, cd, n):
    if c == 0 or c == 1:
        print(c, cd, n)
        assert cd == c
        return 1, 1
    d, order = None, None
    m = int(np.ceil(np.sqrt(n)))
    babies = {}
    power = 1
    for i in range(m):
        if power == 1 and i > 0:
            order = i
            break
        babies[power] = i
        power = power * c % n
    # print(babies)
    cd_im = cd
    one_im = 1
    totient = sympy.totient(n)
    if totient < m:
        cm_inv = 1
        print("AH", totient)
    else:
        cm_inv = pow(c, totient-m, n)
    # print(cm_inv)
    for i in range(m):
        # print(i, cd_im, one_im)
        if d is None and cd_im in babies:
            d = i*m + babies[cd_im]
            # print("d", i, m, babies[cd_im], cd_im, d)
        if order is None and one_im in babies:
            if i != 0 or babies[one_im] != 0:
                order = i*m + babies[one_im]
                # print("order", i, m, babies[one_im], one_im, d)
        if (d is not None) and (order is not None):
            print("n: {}, c: {}, cd: {}, m: {}, cm_inv: {}, d: {}, order: {}".format(n, c, cd, m, cm_inv, d, order))
            return d, order
        cd_im = cd_im * cm_inv % n
        one_im = one_im * cm_inv % n
    print("UH OH")
    if d is not None and order is None:
        order = totient
    print("--- n: {}, c: {}, cd: {}, m: {}, cm_inv: {}, d: {}, order: {}".format(n, c, cd, m, cm_inv, d, order))
    print(babies)
    print("cd_im", [cd * pow(cm_inv, i, n) % n for i in range(m)])
    print("one_im", [pow(cm_inv, i, n) for i in range(m)])
    print("c", [pow(c, i, n) for i in range(n)])





import gmpy2 as gmpy
import binascii
from Crypto.Util import number
import random
import sys
# from secret import flag, seed

flag = "abcdefg"
seed = 0

random.seed(seed)


def urandom(x):
    return random.getrandbits(x*8).to_bytes(x, sys.byteorder)


random.seed(seed)
p = number.getPrime(1024, randfunc=urandom)
q = number.getPrime(1024, randfunc=urandom)

e = 65537

# p = 7
# q = 5
# e = 11

n = p*q
totient = (p-1)*(q-1)
d = int(gmpy.invert(e, totient))
m = int(binascii.hexlify(bytes(flag, encoding='utf-8')), 16)
c = pow(m, e, n)
print(n, d, m, c)
assert pow(c, d, n) == m % n


print("C", c)
print("D", d)
print("N", n)



# from discrete_log import discrete_log, chinese_remainder
import primefac#-fork as primefac
from collections import Counter

# primes = primefac.primes((1 << 12))
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287, 2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423, 2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, 2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, 2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689, 2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741, 2749, 2753, 2767, 2777, 2789, 2791, 2797, 2801, 2803, 2819, 2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 2903, 2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999, 3001, 3011, 3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, 3083, 3089, 3109, 3119, 3121, 3137, 3163, 3167, 3169, 3181, 3187, 3191, 3203, 3209, 3217, 3221, 3229, 3251, 3253, 3257, 3259, 3271, 3299, 3301, 3307, 3313, 3319, 3323, 3329, 3331, 3343, 3347, 3359, 3361, 3371, 3373, 3389, 3391, 3407, 3413, 3433, 3449, 3457, 3461, 3463, 3467, 3469, 3491, 3499, 3511, 3517, 3527, 3529, 3533, 3539, 3541, 3547, 3557, 3559, 3571, 3581, 3583, 3593, 3607, 3613, 3617, 3623, 3631, 3637, 3643, 3659, 3671, 3673, 3677, 3691, 3697, 3701, 3709, 3719, 3727, 3733, 3739, 3761, 3767, 3769, 3779, 3793, 3797, 3803, 3821, 3823, 3833, 3847, 3851, 3853, 3863, 3877, 3881, 3889, 3907, 3911, 3917, 3919, 3923, 3929, 3931, 3943, 3947, 3967, 3989, 4001, 4003, 4007, 4013, 4019, 4021, 4027]
# primes = range(2, 1 << 12)
mods = {}
factor_mods = {}
relevant_primes = {}
prod = 1
for n_p in primes[1:]:
    if prod > n:
        break
    cd = pow(c, d, n_p)
    log = discrete_log(c%n_p, cd, n_p)
    mods[log[1]] = log[0] % log[1]

    p_factors = Counter(primefac.primefac(log[1]))
    # print(p, cd, log, c,d, n)
    
    for p in p_factors:
        current_power = relevant_primes.get(p, 0)
        if p_factors[p] <= current_power:
            continue
        
        ni = p ** p_factors[p]
        mod = log[0] % ni
        # if p_factor in factor_mods:
        #     # print(p_factor, factor_mods[p_factor], mod)
        #     assert mod == factor_mods[p_factor]
        relevant_primes[p] = p_factors[p]
        prod *= p ** (p_factors[p] - current_power)
        factor_mods[ni] = mod
else:
    print("OOPS")
    print(prod > n, math.log10(n), math.log10(prod))

print(mods)
print(relevant_primes)


# ns = list(reversed(list(mods.keys())))
# xs = [mods[n] for n in ns]
# new_d = xs.pop(0)
# prod = ns.pop(0)
# for xi, ni in zip(xs, ns):
#     print("d", d % prod == new_d % prod, d % prod, new_d % prod, prod)
#     print(ni, xi, new_d %ni, prod % ni)
#     new_prod = prod * ni
#     while new_d % ni != xi:
#         new_d += prod
#         if new_d > new_prod:
#             print("UH OH", new_d, ni, prod, xi)
#             print(d % ni, xi)
#             print(d % prod, new_d % prod)
#             assert False
            
#     prod *= ni
#     if prod > n:
#         break
# else:
#     print("OOPS")
    # print(prod > n, math.log10(n), math.log10(prod))


total = 0
for p in relevant_primes:
    ni = p ** relevant_primes[p]
    N = prod // ni
    assert mul_inv(N, ni) * N % ni == 1
    total += factor_mods[ni] * mul_inv(N, ni) * N

print(total% prod)
new_d = total % prod
print("new_d\t", new_d)
print("d    \t", d)



print(new_d % 35)
print(d % 35)

for p in mods.keys():
    if total % p != mods[p]:
        print(p, total % p, mods[p])

prod2 = 1
for p in relevant_primes:
    prod2 *= p**relevant_primes[p]

print(n)
print(prod2)
print(prod2 > n, math.log10(n), math.log10(prod2))

# def chinese_remainder(mods):
#     primes = []
#     
# print(chinese_remainder(mods))
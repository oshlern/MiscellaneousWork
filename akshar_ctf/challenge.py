#!/usr/bin/python3
import gmpy2 as gmpy
import binascii
from secret import flag, seed
from Crypto.Util import number
import sympy
import sys
import random
import numpy as np
sys.dont_write_bytecode = True


def matrix_pow_mod(A, e, n):
    B = np.identity(2, dtype=int)
    mod = np.vectorize(np.mod)
    for bit in bin(e)[2:][::-1]:
        if bit == '1':
            B = mod(B*A, n)

        A = mod(A*A, n)
    return B


def urandom(x):
    return random.getrandbits(x*8).to_bytes(x, sys.byteorder)


random.seed(seed)
p = number.getPrime(1024, randfunc=urandom)
q = number.getPrime(1024, randfunc=urandom)
r = number.getPrime(1024, randfunc=urandom)
n = p*q*r

e = 65537
totient = (p-1)*(q-1)*(r-1)

d = gmpy.invert(e, totient)
# Flags are convenient nonces!
m1 = int(binascii.hexlify(bytes(flag[:len(flag)//2], encoding='utf-8')), 16)
# Flags are convenient nonces!
m2 = int(binascii.hexlify(bytes(flag[len(flag)//2:], encoding='utf-8')), 16)
M1 = np.matrix([[p, q], [r, m1]])
M2 = np.matrix([[p, q], [r, m2]])

c1 = matrix_pow_mod(M1, e, n).tolist()
c2 = matrix_pow_mod(M2, e, n).tolist()
with open("ciphermatrix.txt", "w") as output:
    output.write("n = {}\n\n".format(n))
    output.write("d = {}\n\n".format(d))
    output.write("c1 = {}\n\n".format(c1))
    output.write("c2 = {}\n\n".format(c2))

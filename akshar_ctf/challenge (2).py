#!/usr/bin/python3
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
n = p*q
totient = (p-1)*(q-1)
d = int(gmpy.invert(e, totient))
m = int(binascii.hexlify(bytes(flag, encoding='utf-8')), 16)
c = pow(m, e, n)
assert pow(c, d, n) == m


while True:
    input_str = input(
        "Would you like to: \n1) Get n, e, and c\n2) Decrypt c\n3) Exit\n")
    if input_str.startswith("1"):
        print("n =", n)
        print("e =", e)
        print("c =", c)
    elif input_str.startswith("2"):
        try:
            modulus = int(
                input("What modulus would you like to decrypt with?\n")) % (1 << 12)
        except:
            print("Input format incorrect. Exiting...")
            break

        assert modulus != 0, "Zero is not a valid modulus"
        print(pow(c, d, modulus))

    elif input_str.startswith('3'):
        print("Exiting...")
        break

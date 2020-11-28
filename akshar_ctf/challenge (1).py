#!/usr/bin/python3
import gmpy2 as gmpy
import binascii
from secret import flag, p, q
from Crypto.Util import number
from sympy.ntheory import factorint
import sys
import random
# TODO: Check code for any mistakes


def urandom(x):
    return random.getrandbits(x*8).to_bytes(x, sys.byteorder)


n = p*q
totient = (p-1)*(q-1)
e = number.getPrime(1023, randfunc=urandom)
d = gmpy.invert(e, totient)

m = int(binascii.hexlify(bytes(flag, encoding='utf-8')), 16)
ciphertexts = [str(pow(pt, e, n)) for pt in [m, random.randint(
    2, p-2), random.randint(2, p-2), random.randint(2, p-2), random.randint(2, p-2)]]
random.shuffle(ciphertexts)

print("""Welcome to the {}lottery service! If you choose the right option, you get a FLAG! Otherwise... you get nothing :(.\n\n\n""".format(
    '\u0336'.join(list('rogue '))))

ct = input("""Here are your options. Choose wisely! \n\n{}\n\nYour entry: """.format(
    '\n\n'.join(ciphertexts)))
ct = int(''.join([s for s in ct if s.isdigit()]))
m_test = pow(ct, d, n)
if m_test == m:
    print("\n\nYou don't win lotteries...\n\n... you just don't.")
else:
    print("Oh no! You lost the lottery—unless {} means anything to you. We're all so, so sorry. ".format(m_test))

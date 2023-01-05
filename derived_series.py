from itertools import permutations


n = 5
Zn = list(range(n))
# Zn_str = ''.join(map(str,Zn))
Sn = list(permutations(Zn,n))
# Sn_str = list(map(lambda s: ''.join(s), Sn))

def mult(s1, s2):
    return tuple(s1[i] for i in s2)
# commutators = set()
# for s1 in Sn for s2 in Sn 

s1 = Sn[2]
s2 = Sn[1]
# print(s1)
# print(s2)
# print(mult(s1, s2))
# print(mult(s2, s1))
# print(Sn)


class Permutation:
    def __init__(self, p):
        self.p = tuple(p)
        self.n = len(self.p)
    def __mul__(self, P2):return Permutation(self.p[i] for i in P2.p)
    def inv(self):        return Permutation(self.p.index(i) for i in range(self.n))
    def __str__(self):    return ''.join(map(str,self.p))
    def __eq__(self, P2): return self.p == P2.p
    def __ne__(self, P2): return self.p != P2.p
    def __lt__(self, P2): return self.p <  P2.p
    def __gt__(self, P2): return self.p >  P2.p
    def __le__(self, P2): return self.p <= P2.p
    def __le__(self, P2): return self.p <= P2.p
    def __hash__(self):   return self.p.__hash__()


ps = [Permutation(s) for s in Sn]
print(list(map(str, ps)))

p1 = ps[2]
p2 = ps[1]
print(p1)
print(p2)
print(p1*p2)
print(p2*p1)
# print(p1.inv())

comms = ps
for i in range(5):
    # comms.sort()
    # print(i, list(map(str, comms)))
    # comms = list(set(p1 * p2 * p1.inv() * p2.inv() for p1 in comms for p2 in comms))
    comms2 = set(p1 * p2 * p1.inv() * p2.inv() for p1 in comms for p2 in comms)
    # print(comms2 == comms)
    # comms = comms2

# class Perm:
#     def __init__(self):
#         self.m = True
#         self.a in range(n)
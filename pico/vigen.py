import string

def d(c, k):
    m = ''
    for i in range(len(c)):
        ki = string.ascii_lowercase.index(k[i % len(k)])
        ci = string.ascii_lowercase.index(c[i])
        m += string.ascii_lowercase[ci-ki % 26]
        # m += chr((ord(c[i])-65)+(ord(k[i%len(k)])-65) % 26 + 65)
    return m

m = "vgefmsaapaxpomqemdoubtqdxoaxypeo"
def caesar(m, k):
    c = ''
    for i in range(len(m)):
        mi = string.ascii_lowercase.index(m[i])
        c += string.ascii_lowercase[(mi+k) % 26]
    return c

for i in range(26):
    print(caesar(m, i))
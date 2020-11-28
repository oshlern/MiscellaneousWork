import numpy as np

def discrete_log(c, cd, n):
    if c == 0 or c == 1:
        assert cd == c
        return 1, 1
    d = None
    mod = None
    m = int(np.ceil(np.sqrt(n)))
    # print(n, m)
    babies = {}
    power = 1
    for i in range(m):
        if power == 1 and i > 0:
            mod = i
            break
        babies[power] = i
        power = power * c % n
    y = cd
    one = 1
    # print(babies)
    power = pow(c, n-1-m, n)
    # print(power)
    for i in range(m):
        # print(i, y, one)
        if d is None and y in babies:
            d = i*m + babies[y]
            # print("d", i, m, babies[y], y, d)
            if not mod is None:
                print("n: {}, c: {}, cd: {}, m: {}, power: {}, d: {}, mod: {}".format(n, c, cd, m, power, d, mod) )
                return d, mod
        if mod is None and one in babies:
            if i != 0 or babies[one] != 0:
                mod = i*m + babies[one]
                # print("mod", i, m, babies[one], one, d)
                if not d is None:
                    print("n: {}, c: {}, cd: {}, m: {}, power: {}, d: {}, mod: {}".format(n, c, cd, m, power, d, mod) )
                    return d, mod
        y = y * power % n
        one = one * power % n
    print("UH OH")



def crt(mods, n):
    ns = list(reversed(list(mods.keys())))
    xs = [mods[n] for n in ns]
    new_d = xs.pop(0)
    prod = ns.pop(0)
    for xi, ni in zip(xs, ns):
        while new_d % ni != xi:
            new_d += prod
        prod *= ni
        if prod > n:
            break
    else:
        print("OOPS")
        print(prod > n, math.log10(n), math.log10(prod))
    return new_d, prod

if __name__ == "__main__":
    c = 30
    d = 11
    n = 35
    p = 911
    cd = pow(c, d, p)
    
    # print(discrete_log(c%p, cd, p))

    d = 3419
    mods = {}
    for m in range(19, 100, 7):
        mods[m] = d % m
    print(crt(mods, 100000))
    



# cd = pow(c, d, n)
# print(c, d, n, cd)
# print(discrete_log(c, cd, n))
# knot = [0, 1, 2, 3]
# Are longer knots always less efficient?
# Can a knot be suboptimal at one level but be optimal as a metaknot for a higher level?
# If all patterns are just compositions of the 2-operation ABA'B', then there's no need to use metaknots other than 2,
#  since the metaknots decompose into a 2-metametaknot of metaknots, and thus every composition can be represented as a 2-composition of two knots

def p(n):
    a = [0 for i in range(n+1)]
    k = 1
    a[1] = n
    print("start; k: {}, a: {}".format(k, a))
    i = 0
    while k != 0:
        i += 1
        x = a[k - 1] + 1
        y = a[k] - 1
        k -= 1
        print("\ti{}-  k: {}, x: {}, y: {}, a: {}".format(i, k, x, y, a))
        j = 0
        while x <= y:
            j += 1
            a[k] = x
            y -= x
            k += 1
            print("\t\tj{}-  k: {}, x: {}, y: {}, a: {}".format(j, k, x, y, a))
        a[k] = x + y
        # print("e-  k: {}, x: {}, y: {}, a: {}".format(k, x, y, a))
        yield a[:k + 1]

def partitions(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]

complexities = {
    1: 1,
    2: 4
}

combinations = {
    2: [(1, 1)]
}

# n = 2
# while True:
    # n += 1
for n in range(3, 1000):
    best = float("inf")
    for i in range(1, int(n/2)+1):
        j = n - i
        complexity = 2*(complexities[i] + complexities[j])
        # print(i, j, complexity)
        if complexity == best:
            combs.append((i, j))
        elif complexity < best:
            best = complexity
            combs = [(i, j)]
    complexities[n] = best
    combinations[n] = combs
    print("n: {},\tcomplexity: {},\t combinations: {}".format(n, best, combs))

print(complexities)
import matplotlib.pyplot as plt
import numpy as np
plt.plot(list(complexities.keys()), np.log(list(complexities.values())))
plt.show()

# most_efficient_combinations = {
#     1: [1],
#     2: [2, 2]
# }

# for p in partitions(n):
#     if sum([most_efficient_combinations[i] for i in partition])

# most_efficient = {i: (n, [])}
# def unhook(knot):


# def conjugate(knot):
    


# most_efficient = {
#     1: (1, [[1]]),
#     2: (4, [[1,2,-1,-2]])
# }

# def partitions(n, k):
#     nums = []
#     for k_left in range(k-1, 0, 1):
#         for num in range(1, n - sum(nums) k_left + 1):




# def combine_knots(metaknot, knots):


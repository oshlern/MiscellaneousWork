from fractions import Fraction

nums = [3,4,12]
nums = [Fraction(n) for n in nums]
hist = [nums[:]]
three_fifths = Fraction(3,5)
four_fifths = Fraction(4,5)
while True:
    print(nums)
    i,j = (int(i) for i in input().split())
    a = nums.pop(i)
    b = nums.pop(j)
    nums.append(three_fifths*a - four_fifths*b)
    nums.append(four_fifths*a + three_fifths*b)
    # nums.append(0.6*a - 0.8*b)
    # nums.append(0.8*a + 0.6*b)

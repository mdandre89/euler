# using formula (a+1)(b+1)(c+1)... where a,b,c exponents obtain from factorization of
# n = p**a * q**b * s**c...
# we see that the number of divisor must be larger than 500 = 5**3*2**2
# this implies that our number must be larger than 2**4*3**4*5**4*7*11 = 62370000
# Numbers of the series can be express as n*(n+1)/2; this implies n >= 11168

from collections import Counter
from functools import reduce
import operator

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    c = Counter(factors)
    return reduce(operator.mul, [i+1 for i in c.values()], 1)


def s_n(n):
    return int(n*(n+1)/2)

n = 11168

while prime_factors(s_n(n)) <=500:
    n += 1

print(s_n(n), n)
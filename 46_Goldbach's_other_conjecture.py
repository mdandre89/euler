import math
p_100 = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def isPrime(n):
    if n in p_100:
        return True
    if n % 2 == 0:
        return False
         
    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i== 0:
            return False
    return True

for i in range(1, 10000, 2):
    t = False
    if not isPrime(i):
        for j in range(3, i, 2):
            diff = i - j
            if isPrime(j) and diff % 2 == 0:
                m = (diff//2)
                sq_diff = int(m**0.5)
                if sq_diff**2 == m:
                    t = True
        if not t:
            print('Found', i)
            break
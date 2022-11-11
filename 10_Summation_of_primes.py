import math
 
def isPrime(n):
    if n % 2 == 0:
        return False
         
    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i== 0:
            return False
             
    return True

def sumPrime(n):
    i = 3
    t = 2
    while i <= n:
        if isPrime(i):
            t+=i
        i += 2

    return t

print(sumPrime(2000000))
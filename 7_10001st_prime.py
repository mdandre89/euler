
import math
 
def isPrime(n):
    if n % 2 == 0:
        return False
         
    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i== 0:
            return False
             
    return True

def countPrime(n):
    i = 1
    p = 1
    while p <= n:
        if isPrime(i):
            p+=1
        i += 2

    return i - 2

print(countPrime(10001))
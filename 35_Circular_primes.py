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

result = 0
for i in range(2, 1000000):
    s = str(i)
    l = len(s)
    if all(isPrime(int(s[j:] + s[:j])) for j in range(l)):
        result += 1
        
print(result)
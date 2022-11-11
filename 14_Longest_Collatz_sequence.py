def seq(n):
    i = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        i+=1
    return i

s = 0
number = 0
for i in range(1, 1000000):
    result = seq(i)
    if result > s:
        number = i
        s = result
    
print(number)
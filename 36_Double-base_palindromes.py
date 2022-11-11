

def is_double_palindrome(n):
    s = str(n)
    bs = bin(n)[2:]
    # print(bs, bs[::-1])
    return s == s[::-1] and bs == bs[::-1]


result = 0

for i in range(1, 1000000):
    if is_double_palindrome(i):
        result+=i

print(result)
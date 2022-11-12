i = 0
t = ''
while len(t) <= 1000000:
    t += str(i)
    i += 1

result = int(t[1]) * int(t[10]) * int(t[100]) * int(t[1000]) * int(t[10000]) * int(t[100000]) * int(t[1000000])
print(result)

# Alternative approach, calculate the number and the the right digit in it
def n_digit_costant(n):
    i = 1
    q = 0
    final_number = 0
    while n:
        if i == 1:
            diff = 9 if n >= 10 else n
            n = n - diff
            final_number += diff
        else:
            p = n // i
            q = n % i
            diff = i*9*10**(i-1) if n >= i*9*10**(i-1) else p*i + q
            final_number += 9*10**(i-1) if n >= i*9*10**(i-1) else (p) + (1 if q> 0 else 0)
            n = n - diff
        i += 1
    return str(final_number)[q-1]

result = int(n_digit_costant(1)) * int(n_digit_costant(10)) * int(n_digit_costant(100)) * int(n_digit_costant(1000)) * int(n_digit_costant(10000)) * int(n_digit_costant(100000)) * int(n_digit_costant(1000000))
print(result)
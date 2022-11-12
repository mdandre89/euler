from math import factorial
def sum_factorial_digits(n):
    return sum( int(i) for i in str(factorial(n)))


print(sum_factorial_digits(100))
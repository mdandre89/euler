from math import factorial
def number_of_routes(r, c):
    return int(factorial(r + c) // factorial(r) // factorial(c))


print(number_of_routes(20, 20))
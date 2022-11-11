# Note 3**2 + 4**2 == 5**2; (3*2)**2 + (4*2)**2 = 6**2 + 8**2 = 36 + 64 == 100 == 10**2 == (5*2)**2
# I looked at small pytagorean triplets hoping to find a result that divided 1000
# The pytagorean triplets 8, 15, 17 has a sum of 40 which divides 1000
# so their product by 25(1000//40) satifies both equations.
a = 8*25
b = 15*25
c = 17*25

print(a+b+c, a**2 + b**2 == c**2)
print(a*b*c)
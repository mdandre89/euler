


found = False

for i in range(1000000, 1, -1):
    s = str(i)
    if s == s[::-1] and not found:
        for j in range(999, 900, -1):
            if i % j == 0 and len(str(i//j))==3:
                found = i
                break
print(found)
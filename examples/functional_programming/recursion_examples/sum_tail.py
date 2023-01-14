def s(n, acc=0):
    if n == 0:
        return acc
    else: 
        return s(n - 1, acc + n)

print(s(10))

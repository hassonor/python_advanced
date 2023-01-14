def f(n):
    if n <=1:
        return n
    else:
        return f(n-1) + f(n-2)


print([f(i) for i in range(10)])

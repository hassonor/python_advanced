def f(n, curr=0, next=1):
    if n == 0:
        return curr
    else:
        return f(n - 1, next, curr + next)

print([f(i) for i in range(10)])

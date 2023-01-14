def s(n):
    if n == 0:
        return n
    else: 
        return n + s(n - 1)

# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(10000)

print(s(10))

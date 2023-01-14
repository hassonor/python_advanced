from tramp import tramp

def f(n, curr=0, next=1):
    if n == 0:
        yield curr
    else:
        yield f(n - 1, next, curr + next)

import sys
sys.set_int_max_str_digits(20899)
print(tramp(f, 100_000))

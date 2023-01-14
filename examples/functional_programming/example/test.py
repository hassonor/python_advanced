from functools import reduce

def f1(x):
    print('f1:%s' % x)
    return 11*x

def f2(x):
    print('f2:%s' % x)
    return 22*x

def f3(x):
    print('f3:%s' % x) 
    return 33*x

def f4(x):
    print('f4:%s' % x) 
    return 44*x

x = reduce(lambda g, f: f(g), (f1(5), f2, f3, f4))

def pipe(*args):
    return reduce(lambda g, f: f(g), args)
print(pipe(f1(5), f2, f3, f4))
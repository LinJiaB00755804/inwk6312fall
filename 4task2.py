import functools
def sum(a,b):
    return a + b
def even_sum_in_range(a,b):
    s = functools.reduce(sum,[x for x in range(a,b) if x %2 ==0])
    return s

print(even_sum_in_range(100,500))



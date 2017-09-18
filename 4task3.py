import functools

def sum(a,b):
 return a +b

def even_sum_of_square(a,b):
    s = functools.reduce(sum,[x**2 for x in range(a,b) if x %2 ==0])
    return s

print(even_sum_of_square(0,10))




def filter:
 res=[]
 if isinstance(a,list):
  return a.append(b)
 else:
  return [a,b]


def multiples_of_two(a,b,m):
    s = filter(divided_by_m,[x for x in range(a,b) if x % m ==0])
    return s

print(multiples_of_two(0,10,2))


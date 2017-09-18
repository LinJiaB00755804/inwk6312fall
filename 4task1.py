def nested_sum(t):
    total = 0
    for x in t:
        if isinstance(x, list):
            total = nested_sum(x) + total
        else:
            total += x
    return total

mylist = [1,2,3,[4,5],[6,7,8]]
print(nested_sum(mylist))

def check_fermat(a, b, c, n):
    if n > 2 and (a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")

def values():
    a = int(input("enter a positive integer for a: "))
    b = int(input("enter a positive integer for b: "))
    c = int(input("enter a positive integer for c: "))
    n = int(input("enter a positive integer for n: "))
    return check_fermat(a, b, c, n)

values()

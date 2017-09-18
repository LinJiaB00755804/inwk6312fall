def _triangle(a,b,c):
    if a>b+c or b>a+c or c>a+b:
        print('No')
    elif a == b+c or b == a+c or c == a+b:
        print('degenerate triangle')
    else:
        print('Yes')

def _stick_length():
    a = int(input('enter one integer a:'))
    b = int(input('enter one integer b:'))
    c = int(input('enter one integer c:'))
    return _triangle(a,b,c)
_stick_length()
    

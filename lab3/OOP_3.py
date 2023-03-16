a = -5
b = 5

def f(x):

    return 8 + 2 * x - x * x

def dx():
    
    return 0.1


def _integral (a, b, f, dx, i):

    x = a + i * dx() + dx()/2
    if x > b:
        return 0
    else: 
        return f(x) + _integral(a, b, f, dx, i + 1)


def integral(a, b, f, dx):

    result = _integral(a, b, f, dx, 0) 

    return result * dx()

print(integral(a, b, f, dx))
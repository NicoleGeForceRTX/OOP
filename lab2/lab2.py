def func1(a, b):
    return a * b

def func2(a, b):
    return a - b
    
def calc(f1, f2):
    return lambda a, b: f1(a, b) + f2(a, b)
    
func = calc(func1, func2)
print(func(30, 15))
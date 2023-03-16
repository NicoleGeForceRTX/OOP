
def accumulate(combiner, null_value, not_filter_value, f, a, next, b, filter):
    if (a > b):
        return null_value
    elif not filter(a):
        return combiner(accumulate(combiner, null_value, not_filter_value, f, next(a), next, b, filter), not_filter_value)
    else:
        return combiner(accumulate(combiner, null_value, not_filter_value, f, next(a), next, b, filter), f(a))

def f(x):
    return 45 * x * x  + 27 * x * x * x - 8 * x - 7

def summ(a, b):
    return a + b * dx

def filter(x):
    return x < -3 or x > 2

def next_value(prev_value):
    return prev_value + dx

a = -5
b = 5
dx = 0.5

print(accumulate(summ, 0, 0, f, a + dx / 2, next_value, b, filter))

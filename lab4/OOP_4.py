
def accumulate(combiner, null_value, not_filter_value, f, a, next, b, filter):
    if (a > b):
        return null_value
    elif not filter(a):
        return combiner(accumulate(combiner, null_value, not_filter_value, f, next(a), next, b, filter), not_filter_value)
    else:
        print(a)
        return combiner(accumulate(combiner, null_value, not_filter_value, f, next(a), next, b, filter), f(a))

f = lambda x: 3 * x * x - 2 * x + 5
a = -5
b = 1
dx = 0.5

combiner = lambda a, b: a + b * dx
filter = lambda x: x < -4 or x > -3
next = lambda x: x + dx
print(accumulate(combiner, 0, 0, f, a + dx / 2, next, b, filter))

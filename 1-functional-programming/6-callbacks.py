def apply(func, x, y):
    return func(x, y)


def add(x, y):
    return x + y


print(1 + 2)
print(add(1, 2))
print(apply(add, 1, 2))

# Compilation function


# def compose(f, g):
#     def composed_function(x):
#         return f(g(x))
#     return composed_function


def compose(*funcs):
    def inner(data, funcs=funcs):
        result = data
        for f in reversed(funcs):
            result = f(result)
        return result
    return inner


def times2(num):
    return num * 2


def minus3(num):
    return num - 3


do_both = compose(times2, minus3)

print(do_both(10))

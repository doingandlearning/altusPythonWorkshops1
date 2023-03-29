
# Common Library
import functools
from itertools import groupby
import operator
import timeit

data = [("apple", "fruit"), ("banana", "fruit"), ("tomato", "fruit"),
        ("carrot", "vegetable"), ("potato", "vegetable")]


def find_category(food):
    return food[1]


# for key, group in groupby(data, find_category):
#     print(f"{key}: {[item[0] for item in group]}")

count = 0


@functools.cache
def factorial(n):
    global count
    count += 1
    return n * factorial(n-1) if n else 1


# starttime = timeit.default_timer()
# print("The start time is :", starttime)
# factorial(400)
# print("The time difference is :", timeit.default_timer() - starttime)

# print(count)

# currying ..

def add(x, y):
    return x + y


addFive = functools.partial(operator.add, 5)
print(addFive(10))

# 1 + 1
operator.add(1, 2)
operator.sub

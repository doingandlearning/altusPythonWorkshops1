
import random
import timeit


def square(x):
    return x * x
	
print(square(100))

square_lambda = lambda x: x * x
print(square_lambda(10))

# values = [random.randint(1,100) for _ in range(1000)]

def is_even(number):
	return number % 2 == 0

# starttime = timeit.default_timer()
# [(value * 2) + 4 for value in values if is_even(value)]
# print("The first approach:", timeit.default_timer() - starttime)

# starttime = timeit.default_timer()
# list(map(lambda x: (x * 2) + 4, filter(lambda x: x % 2 == 0, values)))
# print("The second approach :", timeit.default_timer() - starttime)

def multiply(x,y):
	return x * y

mult = lambda x, y: x * y
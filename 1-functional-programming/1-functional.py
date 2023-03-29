num = 5


# 1. Pure functions
def addTen(input):
    return input + 10

# - Same the input will always produce the same output
# - The function should have no side effects!
# - writing to a database
#     - printing to the console
#     - http call


def increaseByTen():
    global num
    num = num + 10


increaseByTen()
addTen(num)
addTen(num)
addTen(num)
addTen(num)
addTen(num)
print(num)

# 2. Immutability

original_list = [1, 2, 3]


def increment_items(input):
    return [item + 1 for item in input]


new_list = increment_items(original_list)

print(original_list)
print(new_list)


# 3. First-class functions
def square(x):
    return x * x


def cube(x):
    return x*x*x


def printResult(func, x):
    print(func(x))


printResult(cube, 10)
printResult(square, 10)


def createAdder(increment):
    return lambda number: number + increment


addFive = createAdder(50)

printResult(addFive, 100)

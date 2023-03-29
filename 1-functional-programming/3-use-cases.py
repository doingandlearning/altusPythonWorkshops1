def square(x):
    return x * x


numbers = [1, 2, 3, 4, 5, 6]
squared_numbers = [square(num) for num in numbers]

print(numbers)
print(squared_numbers)

squared_with_map = list(map(square, numbers))

print(squared_with_map)


def is_even(num):
    return num % 2 == 0


filter_evens = [square(x) for x in list(filter(is_even, numbers))]
print(filter_evens)

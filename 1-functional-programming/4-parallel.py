import concurrent.futures


def square(x):
    return x * x


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(square, data))

print(results)

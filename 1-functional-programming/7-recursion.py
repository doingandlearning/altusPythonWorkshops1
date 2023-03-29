import math
import timeit


def countdown(n):
    if n <= 0:
        print("Liftoff!")
    else:
        print(n)
        countdown(n-1)


countdown(10)

# 5!
# 5 x 4 x 3 x 2 x 1


def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_tail_recursive(n, accumulator=1):
    if n == 0 or n == 1:
        return accumulator
    return factorial_tail_recursive(n-1, accumulator * n)

# Lazy evaluation


factorial_recursive(10)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)


fib(5)
# starttime = timeit.default_timer()
# print("The start time is :", starttime)
# # fib(100)
# print("The time difference is :", timeit.default_timer() - starttime)

numbers = [0, 1, 2, 3, 5, 7, 9, 11, 13, 15]   # Index 3


def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = math.floor((low + high)/2)
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid-1)


print(binary_search(numbers, 7, 0, len(numbers) - 1))

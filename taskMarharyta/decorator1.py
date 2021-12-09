# Task 1
# Implement a decorator `call_once` which runs a function or method once and caches the result.
#
# python
# @call_once
# def sum_of_numbers(a, b):
#     return a + b
#
# print(sum_of_numbers(13, 42))
# >>> 55
# sum_of_numbers(13, 42)
# sum_of_numbers(13, 42)
# sum_of_numbers(13, 42)
import functools


def cacher_func(function):
    cach_tuple = {}
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if args in cach_tuple:
            print('cashed')
            return cach_tuple[args]
        else:
            cach_tuple[args] = function(*args, **kwargs)
            return cach_tuple[args]

    return wrapper

@cacher_func
def sum_of_numbers(a, b):
    c = a + b
    return c

print(sum_of_numbers(5,4))
print(sum_of_numbers(5,4))
print(sum_of_numbers(2,4))
print(sum_of_numbers(3,4))
print(sum_of_numbers(5,4))
print(sum_of_numbers(2,4))

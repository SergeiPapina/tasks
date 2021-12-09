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
    cach = {}
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        flag_cached = 'cached'
        if args not in cach:
            cach[args] = function(*args, **kwargs)
            flag_cached = 'calculated'
        return cach[args], flag_cached
    return wrapper

@cacher_func
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(5, 4))
print(sum_of_numbers(5, 4))
print(sum_of_numbers(2, 4))
print(sum_of_numbers(3, 4))
print(sum_of_numbers(5, 4))
print(sum_of_numbers(2, 4))

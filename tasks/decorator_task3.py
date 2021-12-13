### Task 3
# Create decorator deprecated2 to take an optional argument — a function to call instead of the original function.
#
# Example:
# def deprecated2(...
#
# @deprecated2(new_foo_bar)
# def foo_bar(a, b):
# return a + b
#
# foo_bar(1, 2)
#
# Result:
# foo_bar is deprecated. new_foo_bar will be called instead
# 2

import functools


def deprecated2(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if function.__name__ == 'foo_bar':
            print('foo_bar is deprecated. new_foo_bar will be called instead')
        val = new_foo_bar(*args, **kwargs)
        return val
    return wrapper

@deprecated2
def foo_bar(a, b):
    return a + b

def new_foo_bar(a, b):
    return a + b - 1


print(foo_bar(1, 2))
print(new_foo_bar(1, 2))



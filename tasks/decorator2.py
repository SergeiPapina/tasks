'''
Task 2
Implement the decorator function, which helps to count how many times
the function has occurred.*NOTE:* NOT able to use global variables.@dec
def foo(): passfoo()
foo()
foo()
foo()
r = foo()
print(r)
#>>> 5
'''


from functools import wraps

def count_ch(function, count=[0]):
    """Returns number of times any function with this decorator is called
    """
   # @wraps(function)
    def increase_count(*args, **kwargs):
        count[0] += 1
        return function(*args, **kwargs), count[0]

    return increase_count

def count_check(function, count={}):
    """Returns number of times any function with this decorator is called
    """
    count[function] = 0
   # @wraps(function)
    def increase_count(*args, **kwargs):
        count[function] += 1
        return function(*args, **kwargs), count[function], sum(count.values())

    return increase_count

@count_check
def foo():
    return 42

print(foo(), foo(), foo())

@count_check
def bar():
    return 23

@count_ch
def func(a, b):
    g = a + b
    return g

print(bar(), bar(), bar())
print(foo(), foo(), foo())
print('++++++++++===========+++++++++++++')
print(func(2, 3), func(5,6))

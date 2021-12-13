
def my_decorator(mul):
    def in_func(func):
        def wrapper(*args, **kwargs):
            val = mul*func(*args, **kwargs)
            return val
        return wrapper
    return in_func

@my_decorator(2)
def func(a):
    return a**2

print(func(3))
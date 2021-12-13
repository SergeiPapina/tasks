
def decor(aa):
    def func_processor(func):
        def wrapper(*args, **kwargs):
            value = aa * func(*args, **kwargs)
            return value
        return wrapper
    return func_processor


@decor(7)
def pr():
    return 1

print(pr())







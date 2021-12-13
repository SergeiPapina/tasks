def log(mas=['start', 'end']):
    def decorate(func):
        def wrapper(*args, **kwargs):
            print(mas[0])
            result = func(*args, **kwargs)
            print(mas[1])
            return result
        return wrapper
    return decorate

@log(['begin', 'finish'])
def hi(name):
    print(f"hi, {name}")

hi("Serg")

import builtins

from decorators import do_twice, timer, decodecorator

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper

@timer
@my_decorator
def say_whee(name):
    print("Whee!"+f'{name}')

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

_, j = return_greeting('ghmj')

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

#say_whee = my_decorator(say_whee)
say_whee('Serg')

print(return_greeting('Serii'))


waste_some_time(3)
waste_some_time(50)


#@decodecorator(str, "Decorator for 'stringJoin'", "stringJoin started ...")
def stringJoin(*args):
    st = ''
    for i in args:
        st += i
    return st


p2 = "dfsgkjhkjdfsg dsfg"
p3 = "hello"
print('============')
any_func = decodecorator(int, p2, p3)
oin = any_func(stringJoin)

print('============')

@decodecorator(int, "Decorator for 'summation'\n", "summation started ...")
def summation(*args):
    summ = 0
    for arg in args:
        summ += arg
    return summ


print(stringJoin("I ", 'like ', "Geeks", 'for', "geeks"))
print(" ")
print(summation(19, 2, 8, 533, 67, 981, 119))

ghj = 9

var1 = 2
def hil():
    ghyj = 0
    var1 = 3
    def gh():
         nonlocal var1

         print(var1)
    gh()

if locals() == globals():
    print('ok')

hil()
print(var1)
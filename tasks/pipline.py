# 4. Pipelining Generators
# Multiple generators can be used to pipeline a series of operations. This is best illustrated using an example.
#
# Suppose we have a generator that produces the numbers in the Fibonacci series. And we have another generator for squaring numbers.
#
# If we want to find out the sum of squares of numbers in the Fibonacci series, we can do it in the following way by pipelining the output of generator functions together.

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))
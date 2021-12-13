import sys

nums_squared_lc = [num**2 for num in range(50)]
nums_squared_gc = (num**2 for num in range(50))

print(sys.getsizeof(nums_squared_lc), nums_squared_lc)
print(sys.getsizeof(nums_squared_gc), nums_squared_gc)
try:
    while True:
        print(next(nums_squared_gc))
    # print(next(nums_squared_gc))
    # print(next(nums_squared_gc))
    # print(next(nums_squared_gc))
    # print(next(nums_squared_gc))
    # print(next(nums_squared_gc))
    # print(next(nums_squared_gc))
    # print(next(nums_squared_gc))
except StopIteration:
    print("iteration ended")
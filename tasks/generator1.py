# Task #1
# You must complete the generator function that must increment a counter by 1 each time.
# Also if the argument is supplied (will always be a number) you must then change the counter to that number.
#
# Example:
#
# >>> cnt = gen_counter()
# >>> next(cnt)
# 0
# >>> next(cnt)
# 1
# >>> cnt2 = gen_counter(3)
# >>> next(cnt2)
# 0
# >>> next(cnt2)
# 3
# >>> next(cnt2)
# 6

def gen_counter():
    num = 0
    while True:
        num = yield num
        num += 1
        print("incremented")

par_counter = gen_counter()

a1 = next(par_counter)
a2 = next(par_counter)
a3 = next(par_counter)
print(next(par_counter))
print(next(par_counter))
print(next(par_counter))
par_counter.send(None)
print(par_counter.send(3))

counter = gen_counter()

print(next(counter))
print(next(counter))
print(next(counter))

print(next(par_counter))
print(next(par_counter))
print(next(par_counter))
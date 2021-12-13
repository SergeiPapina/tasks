'''
Task 3
Implement the decorator function, which helps to count how many times the different functions have occurred and count,
for each function, the best time for which function has completed. In the result table, each function
should be possible to mark with associated key-string.
*NOTE:* Able to use global variables.
'''

import functools
import time



def count_func(function):
    #_count_func_execute = 0 # предпочтительно
    count1 = {}
    count1[function] = 0 # нет необходимости

    @functools.wraps(function)
    def increase_count(*args, **kwargs):
        start_time = time.perf_counter()
        count1[function] += 1
        value = function(*args, **kwargs)
        end_time = time.perf_counter()  # 2
        run_time = end_time - start_time
        print(count1)
        return value, count1[function], sum(count1.values()), run_time
    return increase_count

#@count_func
def cyckle1(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

#@count_func
def cyckle2(n, val):
    val_temp = val[0]
    while n > 1:
        val_temp = val_temp / n
        n -= 1
    return val_temp

cyckle1 = count_func(cyckle1)
cyckle2 = count_func(cyckle2)

var1 = cyckle1(70)
var2 = cyckle1(50)
var3 = cyckle2(70, var1)
var4 = cyckle2(70, var1)
var5 = cyckle2(50, var2)
print(var1, '\n', var2)
print(var3, '\n', var4, '\n', var5)


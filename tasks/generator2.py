# Task #2
# Image chocolate bar divided in squares of different sizes.
# Your goal is to take such a bar and determine the minimum number of breaks to reach the threshold as close as possible
# Write the generator that accepts
#     a) an array of numbers
#     b) the number that will determine the threshold.
# The generator should return a number each time and stop by reaching the threshold.
#
# Example:
#
# >>> choco = chocolate(bar=[1, 2, 6, 7, 9, 3], max=12)
# >>> next(choco)
# 9
# >>> next(choco)
# 3
# >>> next(choco)
# StopIteration ==> The Goal is reached
#
# Incorrect behaviour example:
# >>> next(choco)
# 9
# >>> next(choco)
# 2
# >>> next(choco)
# 1
#
# Incorrect, since it could be done in less than 3 breaks

def chocolate(bar_chips, threshold):
    bar_chips.sort()
    bar_sum = bar_chips[-1]  # max(bar_chips)
    ret = bar_chips[-1]
    bar_chips.remove(bar_chips[-1])
    while bar_sum < threshold:
        yield ret
        while bar_sum < threshold:
            if (bar_sum + bar_chips[-1]) > threshold:
                bar_chips.remove(bar_chips[-1])
            else:
                bar_sum += bar_chips[-1]
                ret = bar_chips[-1]
                bar_chips.remove(bar_chips[-1])
                break
    yield ret


choco = chocolate([3, 3, 3, 3, 5], 12)

while True:
    try:
        print(next(choco))
    except StopIteration as error:
        print(error)
        break

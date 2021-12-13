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
import logging
from datetime import datetime
import pathlib
from pathlib import Path
#logging.basicConfig(level=logging.DEBUG)

log_time = datetime.now()
log_file_name = (
        f'{log_time.date().year}' + '_' + f'{log_time.date().month}' + '_' + f'{log_time.date().day}' +
        '_' + f'{log_time.time().hour}' + '_' + f'{log_time.time().minute}' + '_' + f'{log_time.time().second}' +
        '.log'
)
log_path = Path(pathlib.Path(), 'log', log_file_name)

logging.basicConfig(level=logging.INFO, filename=log_path, filemode='w', format='%(name)s - %(levelname)s - %(message)s')
#logging.basicConfig(level=logging.WARNING)

logging.warning('This will get logged to a file')

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

def chocolate(bar_chips, threshold):
    bar_chips.sort(reverse=True)
    ret = 0
    #bar_sum = bar_chips[-1]  # max(bar_chips)
    #ret = bar_chips[-1]
    #bar_chips.remove(bar_chips[-1])
    for chips in bar_chips:
        yield ret
        ret = chips
    yield ret

choco = chocolate([3, 3, 3, 3, 5, 9], 12)

while True:
    try:
        print(next(choco))
    except StopIteration as error:
        print(error)
        break

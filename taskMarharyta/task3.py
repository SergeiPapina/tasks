"""
Task3:
 Implement a function,
 that takes string as an argument and returns a dictionary,
 that contains letters of given string as keys and a number of their occurrence as values.

Example:
 print(count_letters("stringsample"))
 {'s': 2, 't': 1, 'r': 1, 'i': 1,
 'n': 1, 'g': 1, 'a': 1, 'm': 1,
 'p': 1, 'l': 1, 'e': 1}
"""
import sys

def count_letters(inp_str=''):

    outp_dic = {}

    if not inp_str:
        outp_dic['none'] = 0
        return outp_dic

    for let in inp_str:
        outp_dic[let] = inp_str.count(let)

    return outp_dic


print(count_letters("stringsample"))
print(count_letters())
print(count_letters("Happy new year 2022!!!"))
print(sys.path)

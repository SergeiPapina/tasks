"""
Task2:
 Implement a function `get_pairs(lst: List) -> List[Tuple]`
 which returns a list of tuples containing pairs of elements.
 Pairs should be formed as in the example.
 If there is only one element in the list return `None` instead.

Example:
 get_pairs([1, 2, 3, 8, 9])
 [(1, 2), (2, 3), (3, 8), (8, 9)]
 get_pairs(['need', 'to', 'sleep', 'more'])
 [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]
 get_pairs([1])
 None
"""


def get_pairs(inp_list):
    inp_list.append('rt')
    outp_list = []

    if len(inp_list) < 2:
        return 'None'

    prev_x = inp_list[0]
    count = 0
    for x in inp_list:
        if count > 0:
            outp_list.append((prev_x, x))
            prev_x = x
        count = count + 1

    return outp_list



print(get_pairs())
print(get_pairs())

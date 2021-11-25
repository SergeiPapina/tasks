"""
Task1:
 Implement a function
 split_by_index(s: str, indexes: List[int]) -> List[str]
 which splits the `s` string by indexes specified in `indexes`.
 Wrong indexes must be ignored.

Examples:
 split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
 ["python", "is", "cool", ",", "isn't", "it?"]
 split_by_index("no luck", [42])
 ["no luck"]
"""


def split_by_index(inp_str=' ', index_list=[0]):
    outp_list = []
    prev_index = 0

    for index in index_list:
        b = inp_str[prev_index:index]
        if b:
            outp_list.append(b)
            prev_index = index

    b = inp_str[prev_index:]
    if b:
        outp_list.append(b)

    return outp_list


print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
print(split_by_index("no luck", [42]))
print(split_by_index("abrakadabrarazdelis"))
print(split_by_index("abrakadabrarazdelis", [4, 11]))
print(split_by_index('', [11]))


first_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# lis = [num for num in range(10) if num % 2]
lis = [num for num in first_list if not first_list.index(num) % 2]
print('list')
for _ in lis:
    print(_, lis.index(_))
print('generator')




def gen_list(lis):
    for i in lis[1::2]:
        yield i


gen1 = gen_list(first_list)
print('<gen1>')
while True:
    try:
        print(next(gen1))
    except StopIteration as error:
        break
print('</gen1>')


gen = (num for num in first_list if first_list.index(num) % 2)



while True:
    try:
        print(next(gen))
    except StopIteration as error:
        break

print('sorted')

dict_s = {'five':5, 'seven':7, 'two':2, 'one':1, 'three':3, 'four':4, 'eight':8}

sorted_values = sorted(dict_s, key=lambda key: dict_s[key], reverse=False)

sorted_dict = {k: v for k, v in sorted(dict_s.items(), key=lambda key: key[1], reverse=True)}

print(*sorted_values)

for k, v in dict_s.items():
    print(k, v)

print(**sorted_dict)

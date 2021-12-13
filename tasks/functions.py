import dis


def res(a, b, c=1, /, *, d=7, e=2, **kwargs):
    print('a', a)
    print('b', b)
    print('c', c)
    print('d', d)
    print('e', e)
    print('args', kwargs)
    return a + b + c + d + e + kwargs.get('t') + kwargs.get('y') + kwargs.get('u')


print(res(3, 1, e=1, d=4, **{'t': 5, 'y': 6, 'u': 7}))
print(res(3, 1, e=1, d=4, t=5, y=6, u=7))
# print(dis.dis(res))

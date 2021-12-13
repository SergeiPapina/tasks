def permutations(a):
    return combinations(a, len(a))

def combinations(a, n):
    if n == 1:
        for x in a:
            yield [x]
    else:
        for i in range(len(a)):
            for x in combinations(a[:i] + a[i+1:], n-1):
                yield [a[i]] + x

def combinationsNoOrder(a, n):
    if n == 1:
        for x in a:
            yield [x]
    else:
        for i in range(len(a)):
            for x in combinationsNoOrder(a[:i], n-1):
                yield [a[i]] + x

choco = combinationsNoOrder([1, 2, 3, 7, 5, 9], 3)

while True:
    try:
        print(next(choco))
    except StopIteration as error:
        print(error)
        break
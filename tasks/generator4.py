import itertools

def get_sum(vals, comb):
    results = itertools.combinations(set(vals), comb)
    for result in results:
        print(result)
        answer = sum(result)
        if answer == 12:
            print(answer)
            return answer

    comb += 1
    return get_sum(vals, comb)


a = get_sum([1, 3, 3, 3, 3, 5, 6], 3)
print(a)
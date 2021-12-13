import random


def generator(x):
    while True:
        x = yield x + 1
        x += 1

g = generator(5)

# print(next(g))
g.send(None)
print(g.send(10))
print(g.send(7))
print("-------------------------")


def gen_items():
    for item in range(10):
        if not item:
            continue
        try:
            yield item
        except Exception:
            raise Exception("error during generating: %d" % item)

# gen = gen_items()
# for item in gen:
#     if item == 7:
#         gen.throw(ValueError, "bad value")
#     else:
#         print(item)

print("-------------------------")

genn = gen_items()
for item in genn:
    if item == 5:
        genn.close()
    else:
        print(item)

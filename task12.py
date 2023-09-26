# 12_mini_task

def take(func, n):
    res = []
    for i in range(n):
        try:
            res.append(next(func))
        except StopIteration:
            break
    return res


def cycle(iterable):
    while True:
        try:
            yield from iterable
        except TypeError:
            print(f"{type(iterable)} object is not iterable")

print(take(cycle([1,2,3,4]), 15))
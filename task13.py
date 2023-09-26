def chain(*args):
    for iterable in args:
        try:
            yield from iterable
        except TypeError:
            print(f"{type(iterable)} object is not iterable")

print(list(chain([1, 2, 3], ['a', 'b'], (2222, 44424))))

print(list(chain(8, (2222, 44424))))
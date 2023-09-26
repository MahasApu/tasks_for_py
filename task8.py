import functools


def deprecated(f=None, since=None, will_be_removed=None):
    if f is None:
        return functools.partial(deprecated,
                                 since=since,
                                 will_be_removed=will_be_removed)

    def inner(*args, **kwargs):
        print(f'\nWarning: function {f.__name__} is deprecated{f" since version {since}" if since else "."} '
              f'It will be removed in {f"version {will_be_removed}" if will_be_removed else "future versions"}.')
        return f(*args, **kwargs)
    return inner

@deprecated
def bar(x, y):
    print("Hello from bar")
    return x+y


print(bar(4, y=6))


@deprecated(since="4.2.0", will_be_removed="5.0.1")
def loo():
    print("Hello from loo")


loo()


@deprecated(since="4.2.0")
def moo(*args, **kwargs):
    result = 0
    for i in args:
        result += i
    for j in kwargs.values():
        result += j
    print(f"Hello from moo! The sum is {result}")


moo(1000, -122, 33, 5)


@deprecated(will_be_removed="5.0.1")
def foo():
    print("Hello from foo")


foo()
# 14_mini_task
# yield + send = coroutines

import functools


def coroutine(func, *args, **kwargs):
    @functools.wraps(func)
    def inner():
        result = func(*args, **kwargs)
        next(result)
        return result
    return inner


@coroutine
def storage():
    values = set()
    was_there = False

    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)

st = storage()
print(st.send(42))
print(st.send(42))
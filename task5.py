# 5_mini_task


def specialized(func, *args, **kwargs):

    def f(*ar, **kwar):
        return func(*args, *ar, **kwar, **kwargs)
    return f


def sum(*args, **kwargs):
    result = 0
    for i in args:
        result += i
    for j in kwargs.values():
        result += j
    return result


plus_one = specialized(sum, y=1)
print(plus_one(10))

just_two = specialized(sum, 1, 1)
print(just_two())
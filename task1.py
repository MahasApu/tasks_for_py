# 1_mini_task


def devide(count, num, dev):
    while num:
        if num & 1 == dev:
            count += 1
        num = num >> 1
    return count


def counter(x):
    count = 0
    if x > 0:
        return devide(count, num=x, dev=1)

    else:
        x = ~x
        count = 1
        return devide(count, num=x, dev=0)


print(counter(10))
print(counter(-123))
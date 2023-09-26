# 7_mini_task


def flatten(lst, depth, new_lst=None, count=0):

    # Если аргумент просто new_lst=[], то при след. вызове ф-ции
    # значения старого списка сохранятся.
    if new_lst is None:
        new_lst = []

    for i in lst:
        if isinstance(i, list) and count < depth:
            flatten(i, depth, new_lst, count+1)
        else:
            new_lst.append(i)
    return new_lst


print(flatten([1, 2, [4, 5], [6, [7]], 8], depth=1))
print(flatten([1, [2, [4]], [[[5]]], [6, [7, [9, 10, [11]]]], 8], depth=2))

# 6_mini_task


def flatten(lst, new_lst=None):

    # Если аргумент просто new_lst=[], то при след. вызове ф-ции
    # значения старого списка сохранятся.
    if new_lst is None:
        new_lst = []

    for i in lst:
        if isinstance(i, list):
            flatten(i, new_lst)
        else:
            new_lst.append(i)
    return new_lst


print(flatten([1, 2, [4, 5], [6, [7]], 8]))
print(flatten([1, [2, [4]], [[[5]]], [6, [7, [9, 10, [11]]]], 8]))

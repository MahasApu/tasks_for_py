def revDict(d):
    new_d = dict()

    for i in d:
        if d[i] in new_d:
            new_d[d[i]] = new_d[d[i]] + (i,)

        if d[i] not in new_d:
            new_d[d[i]] = (i,)

    for j in new_d:
        if len(new_d[j]) < 2:
            new_d[j] = new_d[j][0]

    return new_d


d = {
    "Ivanov": 97832,
    "Petrov": 55521,
    "Kuznecov": 97832,
    "Surkov": 97832,
    "Egorov": 46579000
}

print(revDict(d))
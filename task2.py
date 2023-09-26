# 2_miniTask


x = [int(i) for i in input().split()]
y = [str(i) for i in input().split()]
z = []

mn = min(len(x), len(y))
for i in range(0, mn):
    z.append((x[i], y[i]))
print(z)

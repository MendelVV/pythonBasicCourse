# методы для работы со списками

a = [1, 'hello', 56, -1, 2.5, [2, 3]]
n = len(a)
print(n)
for i in range(0, n):
    if type(a[i]) == int:
        a[i] += 1
print(a)

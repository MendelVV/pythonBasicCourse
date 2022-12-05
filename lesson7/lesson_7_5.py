#посик в списке
#a.index([элемент], start, end) - индекс первого вхождения элемента
#a.count([элемент]) - количество искомых элементов

a = [1, 3, 2, 1, 1, 9, 3]
#n = a.index(0)
#print(n)
#sz = a.count(1)
#print(sz)
e = 9
if a.count(e)>0:
    n = a.index(e)
    print(n)
else:
    print('Такого элемента нет в списке')
print(3 in a)
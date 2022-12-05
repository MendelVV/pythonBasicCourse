#функция которая для трех множеств находит их объединение
# и вычитает из него их пересечение

def symm_diff(set1, set2, set3=set('asde')):
    res = set1.union(set2, set3)
    res = res.difference(set1.intersection(set2, set3))
    return res

a1 = {10, 60, -2}
a2 = {10, -1, 699}
a3 = {100, -2, 81, 72, 10}

res = symm_diff(a1, a2, set3 = a3)
print(res)
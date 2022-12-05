#Операции над мноджествами
#объединение - s.union(s1, s2, s3, ...)
#пересечение - s.intersection(s1, s2, s3, ...)
#разность - s.difference(s1, s2, s3, ...)

a1 = {9, 82, 0, -900, 100}
a2 = {'772', 80, -0.2, -900, 100, 'op'}
a3 = {'772', 80, -0.2, 'ijs', 100}

r = a1.union(a3, a2)
print(r)
r = a1.intersection(a2)
print(r)
r = a3.difference(a1, a2)
print(r)

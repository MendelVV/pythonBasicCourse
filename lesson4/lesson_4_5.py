#преобразование строк
#lower() - возвращает строку в которой все символы в нижнем регистре
#upper() - возвращает строку в которой все символы в верхнем регистре
#replace(oldstr, newstr, [maxcount]) - заменяет oldstr на newstr в строке и
# возвращает новую строку

s1 = 'HFGdjfGHlds7554'
s2 = s1.lower()
s3 = s1.upper()
print(s1)
print(s2)
print(s3)

s = 'u1 o2 u1 p0 k1 u1 p0'
res = s.replace('u1 ','')
print(s)
print(res)
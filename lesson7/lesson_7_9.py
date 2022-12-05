#map([имя функции], [список])
s = '13;90;-80;32;-100'
a = s.split(';')
print(a)
b = list(map(int, a))
print(b)
print(sum(b))
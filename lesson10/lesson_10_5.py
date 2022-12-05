#map([имя функции], [коллекция]) - применяет [имя функции] ко всем элементам [коллекции]
a = [1, 20, 79, 300, 81]

def my_sqr(x):
    return x*x

r1 = map(my_sqr, a)
r1 = list(r1)
print(r1)

r2 = list(map(lambda x: x**2, a))
print(r2)
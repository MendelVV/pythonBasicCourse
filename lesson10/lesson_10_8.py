#zip([коллекция],[коллекция], ...) - объединяет в коллекцию кортежей

#a1 = [800, -100, 72, 100, 92]
#a2 = [70, -110, -72]
#a3 = [-53, 100, 83, 82]
#a = list(zip(a1, a2, a3))
#print(a)

x = [1.1, 1.2, 1.3, 1.4, 1.5]
y = [2, 3, 4, 5, 6]

for point in zip(x, y):
    print(point)
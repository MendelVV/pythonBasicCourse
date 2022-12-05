#filter([имя функции], [коллекция])#фильтрует коллекцию с помощью указанной функции
b = ['filter', 'map', 'zip', 'list', 'join']

def f_len(s):
    return len(s)>3

if __name__ == '__main__':
    r1 = list(filter(f_len, b))
    print(r1)

    r2 = list(filter(lambda s: len(s)==3, b))
    print(r2)
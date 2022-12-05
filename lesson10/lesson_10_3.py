#переменное количество аргументов

def func(*args):
    print(type(args))
    sum = args[0]
    n = len(args)
    for a in range(1, n):
        sum+=args[a]
    return sum

#w = func(1, 7, 92)
#print(w)

def func2(**args):
    print(type(args))
    print(args['super'])

func2(key1 = 0, w = 100, super = 'super')

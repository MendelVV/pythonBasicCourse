#def [имя функции]([аргументы]):
#    [оператор 1]
#    [оператор 2]
#    ...
#    [оператор n]
#    return [значение]#не обязательно в конце и не обязательно только один раз

#функция которая возводит число в степень
def module():
    print ("ggg")
module()
def power(x=2, n=2):
    res = 1
    for i in range(n):
        res *= x
    return res

r1 = power(n=5, x=3)
print(r1)

r1 = power(n=60, x=3)
print(r1)

r1 = power(3, power(2, 2))
print(r1)
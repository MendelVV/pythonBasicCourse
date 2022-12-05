#вводим числа с клавиатуры до тех пор пока не будет введено end
#для каждого числа проверям является ли оно простым или составным
#выводим ответ и количество простых чисел

s = ''
count = 0#количество простых чисел
while s!='end':
    s = input()
    if not s.isdigit():
        continue
    n = int(s)
    b = False#составное по умолчанию
    for i in range(2, n):
        if n%i==0:
            break
    else:
        b = True#простое
    if b:
        count+=1
        print(str(n)+' простое')
    else:
        print(s+' составное')

print('Введено '+str(count)+' простых чисел')
#вложенные операторы ветвления

#Для двух чисел a и b
#если a>100 увеличть a на 5
#если a>100 и b < 5 возвести b в квадрат
#если a>100 и b > 5 возвести b в куб
#если a<0 умножить b на -1
#если a<10 увеличить a на 100

a = -20
b = 18
if a>100:
    a+=5#a=a+5
    if b<5:
        b**=2
    elif b>5:
        b**=3
elif a<0:
    a+=100
    b*=-1
elif a<10:
    a+=100

#elif a<10:
#    if a<0:
#        b*=-1
#    a+=100

print(a)
print(b)
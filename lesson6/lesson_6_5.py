#break - принудительное завершение цикла

#определить является ли число простым

n = int(input())
b = False
i = 2
while i<n:
    if n%i==0:
        break
    i+=1
else:
    b = True

print(b)

#for i in range(2, n):
#    if n%i==0:
#        print('составное')
#        break
#else:
#    #не вызывали break
#    print('простое')
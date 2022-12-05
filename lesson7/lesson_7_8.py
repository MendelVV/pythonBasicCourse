#s.join([список строк])
#s.split([разделитель])

#a = ['(a', '+', 'b)']
#s = ';;;'
#res = ' '.join(a)
#print(res)

#s1 = 'tra**ta**ta**ooo'
#b = s1.split('ta')
#print(b)

s = '13;90;81;-5;91'
a1 = s.split(';')
print(a1)
sum = 0
for i in a1:
    n = int(i)
    sum += n
print(sum)
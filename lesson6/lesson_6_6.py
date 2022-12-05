#continue - переход к следующему шагу цикла

s = input()
s1 = ''
#n1 = 0

for c in s:
    if not c.isalpha():
        continue
    s1 += c
    if c.isupper():
        print(c*2)
    else:
        print(c*3)
print(s1)
#    if not c.isdigit():
#        continue
#    s1+=c
#    n1+=int(c)

#print(s1)
#print(n1)
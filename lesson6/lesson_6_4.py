#сравнение for и while
#s = 'Hello Word'
#i = 0
#while i<len(s):
#    if s.count(s[i])==1:
#        print(s[i])
#    i+=1

#выводить строки заданные с клавиатуры в верхнем регистре, пока не будет записано "stop"

text = input()

while text!='stop':
    print(text.upper())
    text = input()
print('Всё закончилось')
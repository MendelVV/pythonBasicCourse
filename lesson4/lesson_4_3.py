#len([имя переменной]) - возвращает длину строки

s = "Basic Course"
n = len(s)
print(n)
#find(substr,[start],[end]) - возвращает индекс первого вхождения или -1
#rfind(substr,[start],[end]) - возвращает индекс последнего вхождения или -1
#index(substr,[start],[end]) - возвращает индекс первого вхождения или ValueError
#rindex(substr,[start],[end]) - возвращает индекс последнего вхождения или ValueError
#count(substr,[start],[end]) - возвращает количество непересекающихся подстрок в строке

s = 'Basic se Course'
s1 = 'c'
#index = s.rindex(s1)
sz = s.count(s1)
print(s[::-1])
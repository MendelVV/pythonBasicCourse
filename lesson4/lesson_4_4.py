#Проверка содержимого
#isdigit() - возвращает True если строка состоит только из цифр, иначе - False
#isalpha() - возвращает True если строка состоит только из букв, иначе - False
#islower() - возвращает True если строка состоит только из маленьких букв, иначе - False
#isupper() - возвращает True если строка состоит только из больших букв, иначе - False

tratata = '78290'
b = tratata.isdigit()
print(b)
b = tratata.isalpha()
print(b)
s1 = 'symbols'
b1 = s1.isalpha()
print(b1)
b1 = s1.islower()
print(b1)
s1 = 'FFFFKLL'
b1 = s1.isupper()
print(b1)
s = ''
print(s.isdigit())
print(s.isalpha())
print(s.islower())
print(s.isupper())
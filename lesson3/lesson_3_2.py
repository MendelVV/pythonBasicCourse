n1 = 10
n2 = 50

a1 = n1>n2#False
a2 = True
a3 = n1**2>=n2#True

b = not a2
print(b)
b = a1 and a3
print(b)
b = a1 or a3
print(b)
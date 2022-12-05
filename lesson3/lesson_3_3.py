a1 = False
a2 = True
a3 = True
b = not ((a2 or a3) and a1)
print(b)

n1 = 100
n2 = 100
n3 = 101

c = (not n1 > n3 and a2) or (n1 == n2 or not a2)
print(c)

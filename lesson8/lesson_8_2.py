s1 = {0, 3, 5, 9}
s2 = {3, 0, 3, 9, 5}
s3 = {3, 0, 3, 9, 5, -1}
b1 = s1.issubset(s2)#s1 подмножество s2
print(b1)
b2 = s2.issubset(s1)#s2 подмножество s1
print(b2)
print(s1==s2)
print(s1==s3)
print(s1.issubset(s3))
print(s3.issubset(s1))
b3 = s3.issuperset(s2)#s2 подмножество s3
print(b3)
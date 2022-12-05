s = input()

#x = -1
if s.isdigit():
    d = int(s)
    if d>10:
        x = 100
    else:
        x = 0
elif s.isalpha():
    x = s.lower()
else:
    x = 'No No No'
print(x)
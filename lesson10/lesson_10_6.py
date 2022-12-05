a1 = [800, -100, 72, 100, 92]
a2 = [70, -110, -72]
a3 = [-53, 100, 83, 82]
a = [a1, a2, a3]
print(a)

def m_m(b):
    res = max(b)-min(b)
    return res

r1 = list(map(m_m, a))
print(r1)

r2 = list(map(lambda x: max(x)-min(x), a))
print(r2)
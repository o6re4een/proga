a = []
for i in range(0,7):
    inp = int(input())
    a.append(inp)

a.pop()
del a[0]
print(a)
for el in range(0, len(a)):
    print(el, a[el])
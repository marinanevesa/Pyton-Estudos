a = input()
b = input()
c = input().split()
d = int(c[2])

e = int(c[0])
f = int(c[1])

if d == 1:
    e += 1
else:
    f += 1

print(a, e)
print(b, f)
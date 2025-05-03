a = int(input())
b = int(input())
c = int(input())
d = int(input())

mv = a
if b > mv:
    mv = b
if c > mv:
    mv = c
if d > mv:
    mv = d

mn = a
if b < mn:
    mn = b
if c < mn:
    mn = c
if d < mn:
    mn = d

print("A mais velha tem", mv)
print("A mais nova tem", mn)
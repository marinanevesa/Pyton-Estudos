n = int(input())
a = int(input())
b = int(input())
print('Tabuada do', n, 'de', a, 'até', b)

for i in range(a, b+1):
    c = n * i
    print(n, 'x', i, '=', c)
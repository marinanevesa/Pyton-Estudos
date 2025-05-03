n = int(input())
a = 0

for _ in range(n):
    email = input()
    if '@' not in email:
        a += 1
print(a)

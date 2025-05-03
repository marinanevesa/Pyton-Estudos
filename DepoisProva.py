aprovadas = 0
recuperacao = 0

a = int(input())

for i in range(a):
    b = int(input())
    
    if b >= 3:
        aprovadas += 1
    else:
        recuperacao += 1

print("Aprovadas:", aprovadas)
print("Recuperação:", recuperacao)
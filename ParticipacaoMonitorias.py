a = int(input())
b = []
c = ""
d = []

for i in range(a):
    nome = input()
    b.append(nome)
    
    for j in range(4):
        monitoria = int(input())
        d.append(monitoria)

    if all(g >= 120 for g in d[i*4:(i*4)+4]):
        c = b[i]
        print(c, "tem monitorias OK! :-)")
    else:
        c = b[i]
        print(c, "não tem monitorias suficientes :-(")
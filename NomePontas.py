nomes = []
nome = input()

while nome != '.':
    nomes.append(nome)
    nome = input()

nomes.sort()

if len(nomes) > 0:
    primeira_menina = nomes[0]
    ultima_menina = nomes[-1]
    print( primeira_menina)
    print( ultima_menina)
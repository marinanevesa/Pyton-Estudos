def contar():
    X = 0
    N = 0
    M = 0
    T = 0
    
    while True:
        a = input()
        if a == '.':
            break
        if a == 'X':
            X += 1
        elif a == 'N':
            N += 1
        elif a == 'M':
            M += 1
        T += 1
    print("Abaixo do peso:", X)
    print("Peso normal:", N)
    print("Acima do peso:", M)
    print("Total de crianças:", T)
contar()
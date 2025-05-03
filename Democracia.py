def a():
    b = int(input())
    c = 0
    d = 0
    e = 0
    f = 0
    for _ in range(b):
        g = input()

        if g == 'X':
            c += 1
        elif g == 'Y':
            d += 1
        elif g == 'B':
            e += 1
        elif g == 'N':
            f += 1     
    print("X ", c)
    print("Y ", d)
    print("Brancos e nulos ", e + f)

    if c > d:
        print("vitoria: X")
    elif d > c:
        print("vitoria: Y")
    else:
        print("empate!")


a()

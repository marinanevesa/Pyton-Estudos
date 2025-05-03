n = int(input())
while True:
    a = input()

    if a == "":
        break

    a = int(a)

    if a == n:
        print('igual')
        break
    elif a < n:
        print('maior')
    else:
        print('menor')
        
def a():
    b = input()  
    c = 0
    d = input()
    while d != b:
        c += 1
        d = input() 
    return c
e = a()
print(e)

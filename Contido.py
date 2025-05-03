a = input("")
b = input("")
c = input("")

if a in b and a in c:
    print(a, "CONTIDO EM", b, "E", a, "CONTIDO EM", c)
elif a in b and a not in c:
    print(a, "CONTIDO EM", b, "MAS", a, "NÃO CONTIDO EM", c)
elif a not in b and a in c:
    print(a, "NÃO CONTIDO EM", b, "MAS", a, "CONTIDO EM", c)
elif a not in b and a not in c:
    print(a, "NÃO CONTIDO EM", b, "E", a, "NÃO CONTIDO EM", c)

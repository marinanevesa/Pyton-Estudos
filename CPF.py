a = input()
a = a.replace(".", "")
a = a.replace("-", "")

if len(a) != 11:
    print(a)
    print("ERROR")
else:
    print(a)
    print("OK")
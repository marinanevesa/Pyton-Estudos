a = input("")
b = int(input(""))
c = int(input(""))

if a == '+':
    resultado = b + c
elif a == '-':
    resultado = b - c
elif a == '*':
    resultado = b * c
elif a == '/':
    resultado = b / c
elif a == '//':
    resultado = b // c
elif a == '%':
    resultado = b % c
elif a == '**':
    resultado = b ** c

print(resultado)
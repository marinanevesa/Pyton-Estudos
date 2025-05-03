caracter = input()

if caracter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
    print("vogal")
elif caracter in ['@', '#', '$', '%', '&', '*', '(', ')', '_', '-', '+', '=', '!']:
    print("especial")
elif caracter in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
    print("algarismo")
else:
    print("outro")
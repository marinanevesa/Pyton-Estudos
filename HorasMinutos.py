minutos = int(input())

a = minutos // 60
b = minutos % 60

print('{}min = {}h{}min'.format(minutos, a, b))
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c)
        s += c
        cont += 1
print('O somatório dos {} números é: {}'.format(cont, s))
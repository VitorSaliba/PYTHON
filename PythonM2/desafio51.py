primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimoTermo = primeiroTermo + (10 - 1) * razao

for c in range(primeiroTermo, decimoTermo + razao, razao):
    print('{} '.format(c), end = '-> ')
print('ACABOU')

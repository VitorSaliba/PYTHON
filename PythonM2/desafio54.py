from datetime import date
atual = date.today().year
maior = 0
menor = 0

for c in range(1, 8):
    ano = int(input('Digite o ano que a {} pessoa nasceu: '.format(c)))
    idade = atual - ano
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} pessoas menores de idade.\nE também {} pessoas maiores de idade.'.format(menor, maior))
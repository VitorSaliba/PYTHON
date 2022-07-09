continuar = 'S'
cont = soma = maior = menor = 0

while continuar == 'S':
    n = int(input('Digite um número: '))
    continuar = str(input('Quer continuar [S/N] : ')).strip().upper()[0]
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / cont
print('Média: {}\nMaior: {}\nMenor: {}'.format(media, maior, menor))
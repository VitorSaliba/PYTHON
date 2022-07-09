tot = maisMil = cont = menor = 0
barato = ''
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    tot += preco
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    if preco >= 1000:
        maisMil += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] : ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total gasto na compra foi R${tot:.2f}')
print(f'Temos {maisMil} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
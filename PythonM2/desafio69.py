contI = contH = contM = 0
while True:
    print('CADASTRE UMA PESSOA')
    idade = int(input('Idade: '))
    if idade >= 18:
        contI += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F] : ')).strip().upper()[0]
    if sexo == 'M':
        contH += 1
    elif sexo == 'F' and idade < 20:
        contM += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N] : ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {contI}')
print(f'Ao todo temos {contH} homens cadastrados.')
print(f'E temos {contM} mulheres com menos de 20 anos.')
maiorIdadeHomem = 0
nomeVelho = ''
menorVinte = 0
somaIdade = 0
mediaIdade = 0
for p in range(1, 5):
    print('{} pessoa: '.format(p))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo (M/F): ')).strip()
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        menorVinte += 1
       
mediaIdade = somaIdade / 4
    
print('A média da idade do grupo é {} anos'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeHomem, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(menorVinte))
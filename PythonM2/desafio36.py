valorCasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário? R$'))
quantosAnos = int(input('Em quantos anos vai ser pago? '))

prestacaoMensal = (valorCasa / (quantosAnos * 12))

if prestacaoMensal >= ((salario * 30) / 100):
    print('Empréstimo negado! O valor da prestação mensal é R${:.2f} e excede 30% do seu salário.'.format(prestacaoMensal))
else:
    print('Empréstimo aceito! Prestação mensal: R${:.2f}'.format(prestacaoMensal))
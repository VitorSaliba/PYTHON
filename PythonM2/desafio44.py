preco = float(input('Digite o preço normal do produto: '))
condicao = int(input('Digite 1 para à vista no dinheiro/cheque\nDigite 2 para à vista no cartão\nDigite 3 para 2x no cartão\nDigite 4 para 3x ou mais no cartão\n'))

if condicao == 1:
    desconto = preco - ((10 * preco) / 100)
    print('O valor era {} e passou a ser {} com 10% de desconto.'.format(preco, desconto))
elif condicao == 2:
    desconto = preco - ((5 * preco) / 100)
    print('O valor era {} e passou a ser {} com 5% de desconto.'.format(preco, desconto))
elif condicao == 3:
    cartao = preco / 2
    print('O valor é de {} e em 2x fica {}'.format(preco, cartao))
elif condicao == 4:
    juros = preco + ((20 * preco) / 100)
    print('O valor de {} sofre um acréscimo de 20% de juros e passa a ser {} em 3x ou mais no cartão'.format(preco, juros))
else:
    print('Digite um número válido')
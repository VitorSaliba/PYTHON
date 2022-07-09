import random
computador = random.randint(0, 10)
tentativas = 0
palpite = int(input('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?\nQual seu palpite? '))
while palpite != computador:
    if palpite < computador:
        palpite = int(input('Mais... Tente outra vez: '))
        tentativas += 1
    else:
        palpite = int(input('Menos... Tente outra vez: '))
        tentativas += 1
tentativas += 1
print('Acertou com {} tentativas. Parabéns!'.format(tentativas))
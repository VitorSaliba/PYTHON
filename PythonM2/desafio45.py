import random

jogador = str(input('Pedra, papel ou tesoura? '))
computador = random.randint(1, 3)

if computador == 1:
    computador = 'pedra'
elif computador == 2:
    computador = 'papel'
elif computador == 3:
    computador = 'tesoura'

if computador == 'pedra' and jogador == 'papel':
    print('O computador escolheu {} e você escolheu {}. Você venceu!'.format(computador, jogador))
elif computador == 'tesoura' and jogador == 'pedra':
    print('O computador escolheu {} e você escolheu {}. Você venceu!'.format(computador, jogador))
elif computador == 'papel' and jogador == 'tesoura':
    print('O computador escolheu {} e você escolheu {}. Você venceu!'.format(computador, jogador))
elif computador == 'papel' and jogador == 'pedra':
    print('O computador escolheu {} e você escolheu {}. Você perdeu!'.format(computador, jogador))
elif computador == 'pedra' and jogador == 'tesoura':
    print('O computador escolheu {} e você escolheu {}. Você perdeu!'.format(computador, jogador))
elif computador == 'tesoura' and jogador == 'papel':
    print('O computador escolheu {} e você escolheu {}. Você perdeu!'.format(computador, jogador))
else:
    print('O computador escolheu {} e você escolheu {}. Empate!'.format(computador, jogador))
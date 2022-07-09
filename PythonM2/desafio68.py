import random

vit = 0

while True:
    print('Vamos jogar par ou ímpar')
    jogador = int(input('Diga um valor: '))
    condicao = str(input('Par ou ímpar? [P/I] : ')).strip().upper()[0]
    computador = random.randint(1, 10)
    if condicao == 'P' and (jogador + computador) % 2 == 0:
        print(f'Você escolheu {jogador} e o computador {computador}. Total de {jogador + computador} DEU PAR\nVOCÊ VENCEU!')
        vit +=1
    else:
        print(f'Você escolheu {jogador} e o computador {computador}. Total de {jogador + computador} DEU ÍMPAR\nVOCÊ PERDEU!')
        break
    if condicao == 'I' and (jogador + computador) % 2 != 0:
        print(f'Você escolheu {jogador} e o computador {computador}. Total de {jogador + computador} DEU ÍMPAR\nVOCÊ VENCEU!')
        vit += 1
    else:
        print(f'Você escolheu {jogador} e o computador {computador}. Total de {jogador + computador} DEU PAR\nVOCÊ PERDEU!')
        break
print(f'GAME OVER. Você perdeu com um total de {vit} vitórias!')
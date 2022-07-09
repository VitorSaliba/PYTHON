while True:
    tabuada = int(input('Digite um número para ver sua tabuada: '))
    if tabuada < 0:
        break
    for count in range(1, 11):
        print(f'{tabuada} x {count} = {tabuada*count}')
print('Fim do programa!')
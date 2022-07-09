v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
soma = 0
multiplicacao = 0
maior = 0
opcao = 0

while opcao != 5:
    opcao = int(input('Digite 1 para somar.\nDigite 2 para multiplicar.\nDigite 3 para ver o maior.\nDigite 4 para inserir novos numeros.\nDigite 5 para sair do programa.\n'))
    if opcao == 1:
        soma = v1 + v2
        print('O resultado de {} + {} é {}'.format(v1, v2, soma))
    elif opcao == 2:
        multiplicacao = v1 * v2
        print('O resultado de {} x {} é {}'.format(v1, v2, multiplicacao))
    elif opcao == 3:
        if v1 > v2:
            maior = v1
            print('Entre {} e {} o maior valor é {}'.format(v1, v2, v1))
        elif v1 < v2:
            maior = v2
            print('Entre {} e {} o maior valor é {}'.format(v1, v2, v2))
        else:
            print('Os valores são iguais!')
    elif opcao == 4:
        v1 = int(input('Informe o primeiro valor novamente: '))
        v2 = int(input('Informe o segundo valor novamente: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida!')
print('Fim do programa!')
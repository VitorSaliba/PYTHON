n = int(input('Digite um número inteiro: '))

baseConversao = int(input('Digite 1 para conversão binária\nDigite 2 para conversão octal\nDigite 3 para conversão hexadecimal\n'))

if baseConversao == 1:
    binario = format(n, "b")
    print('O número digitado na base binária é: {}'.format(binario))
elif baseConversao == 2:
    octal = format(n, "o")
    print('O número digitado na base octal é: {}'.format(octal))
elif baseConversao == 3:
    hexa = format(n, "x")
    print('O número digitado na base hexadecimal é: {}'.format(hexa))
else:
    print('Opção inválida!')
    
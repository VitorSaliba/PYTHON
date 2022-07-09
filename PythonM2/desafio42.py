l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 == l3:
        print('Os segmentos PODEM FORMAR um triângulo EQUILÁTERO')
    elif l1 != l2 != l3 != l1:
        print('Os segmentos PODEM FORMAR um triângulo ESCALENO')
    else:
       print('Os segmentos PODEM FORMAR um triângulo ISÓSCELES')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo')
from datetime import date

atual = date.today().year

ano = int(input('Digite o ano do seu nascimento: '))

idade = atual - ano

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} ano(s) para o alistamento'.format(saldo))
    anoA = atual + saldo
    print('Seu alistamento será em {}'.format(anoA))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} ano(s)'.format(saldo))
    anoA = atual - saldo
    print('Seu alistamento foi em {}'.format(anoA))
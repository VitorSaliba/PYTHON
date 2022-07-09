from datetime import date

atual = date.today().year

ano = int(input('Digite o ano do seu nascimento: '))

idade = atual - ano

if idade > 0 and idade <= 9:
    print('Você tem {} ano(s) e se encaixa na categoria MIRIN'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} ano(s) e se encaixa na categoria INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você tem {} ano(s) e se encaixa na categoria JÚNIOR'.format(idade))
elif idade > 19 and idade <= 20:
    print('Você tem {} ano(s) e se encaixa na categoria SÊNIOR'.format(idade))
else:
    print('Você tem {} ano(s) e se encaixa na categoria MASTER'.format(idade))
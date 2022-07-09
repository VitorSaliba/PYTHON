nome = str(input('Qual é seu nome? '))
if nome == 'Vitor':
    print('Que nome bonito!')
elif nome == 'Guilherme' or nome == 'João' or nome == 'Luiz':
    print('Parabéns, você é gay!')
else:
    print('Seu nome é bem normal!')

print('Tenha um bom dia, {}!'.format(nome))
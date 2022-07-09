sexo = str(input('Digite seu sexo (M/F): ')).strip().upper() [0]

while sexo not in 'MF':
    sexo = str(input('Dados inválidos! Por favor, informe seu sexo (M/F): ')).strip().upper() [0]
if sexo in 'M':
    print('Você é do sexo masculino.')
else:
    print('Você é do sexo feminino.')
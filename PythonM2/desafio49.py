tabuada = int(input('Digite um número para ver sua tabuada: '))

for count in range(1, 11):
    print("%d x %d = %d" % (tabuada, count, tabuada*count) )
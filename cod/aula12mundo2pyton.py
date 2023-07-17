from os import name

nome = str(input('Qual é o seu nome? '))
if nome == 'Erika':
    print('Que nome lindo!')
elif nome == 'Carlos':
    print('Seu nome é popular no Brasil!')
elif nome in 'Maria Pedro Jesus Joao':
    print('Esse nome é católico.')
else:
    print('Que nome comum!')
print('Tenha um excelente dia, {}!'.format(nome))
#if e else sao condicoes comum, elif é uma condicional aninhada



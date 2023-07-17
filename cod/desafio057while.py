sexo = str(input('Digite seu sexo: [F/M] ' )).strip().upper()[0]
print(sexo)
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Digite F ou M para escolher o sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))

'''if sexo == 'F':
            print('Você escolheu o sexo Feminino')
    if sexo == 'M':
        print('Você escolheu o sexo Masculino')'''


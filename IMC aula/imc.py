p = int(input('Digite o peso: '))
h = float(input('Digite a altura: '))
imc = float(p/(h*h))
print('O Resultado do seu IMC é: {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif 18.6 <= imc <= 24.9:
    print('Você está dentro do peso ideal')
elif 24.9 < imc <= 29.9:
    print('Você está acima do peso ideal')
elif 29.9 < imc <= 34.9:
    print('Você está dentro da obesidade grau I')
elif 34.9 < imc <= 39.9:
    print('Você está dentro da obesidade grau II ')
elif imc > 40:
    print('Você está dentro da obesidade mórbida')
else:
    print('Valor nao encontado')


try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except(ValueError, TypeError):
    print('Tivemos um problemas com os dados que o usuário digitou')
except ZeroDivisionError:
    print('Nao é possivel dividir o número digitado por zero')
except KeyboardInterrupt:
    print('O usuário nao informou os dados')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre, muito obrigado!')

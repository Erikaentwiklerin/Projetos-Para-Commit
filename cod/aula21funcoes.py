#docstrings informa para que serve o comando

#print(input.__doc__)
#help(input)
'''from time import sleep
def contador(i, f, p):
    #docstring catalogo minha funcao e posso até colocar quem criou como o exemplo abaixo
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da comntagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    funcao criada na aula do prof Guanabara do CursoemVideo
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
        sleep(0.3)
    print('FIM')


help(contador)'''

#parametros opcionais

#escopo de variáveis

'''def teste(b):
    a = 8
    b += 4
    c = 2
    print(f'Na funcao teste, A vale {a}')
    print(f'Na funcao teste, B vale {b}')
    print(f'Na funcao teste, C vale {c}')



#programa principal
a = 5
teste(a)
print(f'A fora vale {a}')
# n é uma variável global, foi declarada na funcao e no programa principal
# se a variável é declarada somente na funcao, chama-se, variável local.
# mesmo se uma variável for declarada apenas no programa principal, ela faz parte do escopo global'''


'''def funcao():
    n1 = 4
    print(f'N dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {n1}.')


#usando variáveis globais como globais


def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'Na funcao teste, A vale {a}')
    print(f'Na funcao teste, B vale {b}')
    print(f'Na funcao teste, C vale {c}')

#o a assume o valor 8 dentro e fora (global e local), usando a palavra global

#programa principal
a = 5
teste(a)
print(f'A fora vale {a}')'''


#retorno de valores


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foma: {r1}, {r2} e {r3}')

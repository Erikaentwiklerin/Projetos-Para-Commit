#funcoes sao criadas quando temos sempre uma rotina
def titulo(txt):
    print('-='*30)
    print(txt)
    print('-='*30)


titulo('   Erika    ')
titulo('   Programmer     ')

#rotina de contas de somar
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma entre {a} e {b} vale: {s}')


soma(b=4, a=5)
soma(8, 9)
soma(2, 1)
#funcoes de tupla
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} que sao ao todo {tam} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

#funcoes de lista
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)






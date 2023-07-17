#FATIAMENTO
#tuplas sao imutáveis
#na tupla posso usar str ou numeros int ou float tudo junto, claro, separados por vírgula e ''
#para apagar qualquer variável da memória em Python uso o del(variável)

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
'''print(lanche)
#posso representar a tupla sem ().

print(lanche[-2])

print(lanche[1:3])
#fatiamento mosta do 1 até o elemento 3 ignorando o ultimo

print(lanche[:2])
# vai ir do primeiro até o 2 ignorando o 2

print(lanche[2:])
#vai do 2 até o fim'''

#print(len(lanche)) # len é o comprimento da variável
#for comida in lanche:
    #print(f'Eu vou comer: {comida} ')
'''for cont in range(0, len(lanche)):
    print('Eu vou comer {lanche[cont]} na posicao {cont}')
print('Comi pra caramba!')'''

#outras formas com o mesmo resultado:

'''for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi muito!!')'''

'''for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')
print('Comi pra caramba!')'''

a = 2, 5, 4
b = 5, 8, 1, 2
c = b + a  #na tupla ele vai juntar os elementos ,a ordem em que é colocada
print(c)
print(c.count(5)) # .count vai mostrar quantas vezes aparece o numero 5
print(c.index(8)) #mostra a posicao que está o 8
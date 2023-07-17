print('\033[33mOlá Mundo!\033[m')
a = 3
b = 5
#print('Os valores sao \033[32m{}\033[m e \033[35m {}\033[m!!!!!'.format(a, b))
cores = {'limpa':'\033[m', 'azul':'\033[34m','amarelo':'\033[33m','pretoebranco':'\033[7;30m'}
nome = 'Erika Amorim'
print('Que lindo seu nome {}{}{}!!!'.format(cores['azul'], nome, cores['limpa'] ))
# O \033[m finaliza o codigo.
# também posso guardar as cores nas variaveis como dicionario como codigo exemplo a cima:

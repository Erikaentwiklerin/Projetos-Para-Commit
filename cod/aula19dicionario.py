pessoas = {'nome': 'Erika', 'sexo': 'M', 'idade': 22}
pessoas['nome'] = 'Ana' # aqui eu substituí o nome Erika por Ana
pessoas['peso'] = 78 # adicionei um objeto
print(pessoas['nome'])
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items()) #funciona como o enumerate em listas
print('-='*30)
for k, v in pessoas.items():
    print(f'{k} = {v}')

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('sigla do Estado:'))
    brasil.append(estado.copy()) # copia os dados do estado, em lista faria isso com [:]
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

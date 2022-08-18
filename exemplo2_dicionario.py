# cpf - nome

pessoas = {'123456': 'Paulo', '6797465': 'Maria', '333444': 'Pedro'}
print(pessoas)

print(pessoas['123456'])

# alterando
pessoas['123456'] = 'Paulo Vieira'
print(pessoas)

# inserir
pessoas['999777'] = 'João'
print(pessoas)

# cadastro
'''
pessoas = {}
for n in range(3):
    cpf = input('CPF: ')
    nome = input('NOME: ')
    pessoas[cpf] = nome         # insere no dicionario
print(pessoas)
'''

# excluir
pessoas.pop('999777')
print(pessoas)

# percorrer dicionario
for chave in pessoas:
    print(chave, pessoas[chave])

if '123456' in pessoas:
    print('cpf cadastrado: ', pessoas['123456'])
else:
    print('cpf não cadastrado')


# dicionario contendo o ra e uma lista de notas:
alunos = {123456: [10, 7, 8, 9], 456789: [4, 6.5, 3, 9]}
print(alunos[456789])

# altera a nota de um aluno
alunos[456789][0] = 10
print(alunos)

# insere uma nova nota para um aluno
alunos[456789].append(6)
print(alunos)

# ordena as notas de um alunos
alunos[456789].sort()
print(alunos)
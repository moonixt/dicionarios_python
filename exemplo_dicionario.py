# EXEMPLO DE DICIONÁRIO

# Exemplo de dicionario para armazenar um cadastro de pessoas (CPF e NOME)
cadastro = {'12345678': 'Paulo', '88888888': 'Maria', '4565456': 'João'}

# Exibir dicionário
print(cadastro)

# Exibir valor de uma chave específica
print(cadastro['12345678'])

# Adicionar novos itens
cadastro['99999999'] = 'Ana'
cadastro['77777777'] = 'Pedro'
print(cadastro)

# Alterar valor de um item
cadastro['99999999'] = 'Ana Maria'
print(cadastro)

# Excluir item
cadastro.pop('12345678')
print(cadastro)

# Verificar se chave existe no dicionário
if '99999999' in cadastro:
    print('CPF cadastrado')
else:
    print('CPF não cadastrado')

# Percorrer chaves do dicionário
for chave in cadastro:
    print(chave, cadastro[chave])

# Preencher dicionário com dados informados pelo usuário
cadastro = {}                           # dicionário vazio
for a in range(3):
    cpf = input('CPF: ')                # solicita a chave
    nome = input('Nome: ')              # solicita o valor
    cadastro[cpf] = nome                # insere chave e valor no dicionário
print(cadastro)


# Dicionário que armazena lista (nome e notas de alunos)
alunos = {'Paulo': [9, 8, 7, 4, 10],
          'Maria': [8, 3, 8, 9, 10],
          'Pedro': [10, 7, 6, 4, 8]}
print(alunos)

# Exibir lista de notas de um aluno
print(alunos['Pedro'])

# Inserir uma nova nota para um aluno
alunos['Pedro'].append(10)
print(alunos)

# Alterar a nota de um aluno
alunos['Pedro'][0] = 9.5
print(alunos)
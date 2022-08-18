'''
Preencha um dicionário com as informações de 5 produtos.
- Utilize o ​nome​ do produto como chave e o ​preço​ como valor.
- Solicite os dados ao usuário
Percorra o dicionário e exiba o nome dos produtos com preço maior que R$ 50.00
'''

produtos = {}

for i in range(5):
    nome = input("Informe o nome do produto: ")
    preco = float(input("Informe o preço do produto: "))
    produtos[nome] = preco

print(produtos)

for chave in produtos:
    if produtos[chave] > 50:
        print(chave, produtos[chave])
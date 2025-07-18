dicionario_produtos = {}

for i in range(5):
    nome_produto = str(input("Digite o nome do produto: "))
    preco_produto = float(input("Digite o preço do produto: "))

    dicionario_produtos[nome_produto] = preco_produto
    
valor_total = sum(dicionario_produtos.values())

print(f"Valor total: R${valor_total:.2f} Reais")
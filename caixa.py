# Nesse projeto sera criado um simulador de caixa de supermercado simples sem DB, usaremos apenas python simples.

produtoevalor = {"arroz": 5.50, "feijao": 4.50, "oleo": 8.00}

produto = ""

listaproduto = []

valor = 0


while produtoevalor != "sair":
   produto = input("Digite o nome do produto: ")
   valor = produtoevalor.get(produto)

   print (f"R$ {valor:.2f}")


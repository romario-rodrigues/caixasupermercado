# Nesse projeto sera criado um simulador de caixa de supermercado simples sem DB, usaremos apenas python simples.

produtoevalor = {"arroz": 5.50, "feijao": 4.50, "oleo": 8.00}

produto = ""

carrinho = []

valor = []

total = []


while True:
   produto = input("Digite o nome do produto: ")
   if produto == "sair":
      for itens in carrinho:
         print(itens)
      break
   valor = produtoevalor.get(produto)
   carrinho.extend([produto, valor])
   total.append(valor)

   
   print(f"TOTAL: R$ {sum(total):.2f}")
   

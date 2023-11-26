# Nesse projeto sera criado um simulador de caixa de supermercado simples sem DB, usaremos apenas python simples.

produtoevalor = {"arroz": 5.50, "feijao": 4.50, "oleo": 8.00}

produto = ""

carrinho = []

valor = []

total = []


while True:
   
   produto = input("Digite o nome do produto: ")
   
   
   if produto == "sair":
      break
   
   else:
    quantidade = int(input("Digite a quantidade: "))
    valor = produtoevalor.get(produto)
    carrinho.extend([produto, valor])
    total.append(quantidade * valor)
    

    
    print(f"TOTAL: R$ {sum(total):.2f}")

for compra in carrinho:
  print(compra)
print(f"Total a Pagar R$ : {sum(total):.2f}")
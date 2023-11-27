# Nesse projeto será criado um simulador de caixa de supermercado simples sem DB, usaremos apenas python simples.

produtoevalor = {"arroz": 5.50, "feijao": 4.50, "oleo": 8.00}

produto = ""

carrinho = []

valor = []

total = []

quantiitens = [] 



while True:
   
   produto = input("Digite o nome do produto: ")
   
   
   if produto == "sair":
      break
   
   else:
    quantidade = int(input("Digite a quantidade: "))
    valor = produtoevalor.get(produto)
    carrinho.extend([produto])
    total.append(quantidade * valor)
    quantiitens.append(quantidade)

    print(f"TOTAL: R$ {sum(total):.2f}")

print("-" * 30)
print('CUPOM FISCAL\n')

print('CÓD ITEM. DESC.\n')

for c in range(0, len(quantiitens)):
  print(c + 1, quantiitens[c],  carrinho[c], total[c])

print("-" * 30, "\n")
print(f"Total a Pagar R$ : {sum(total):.2f}")

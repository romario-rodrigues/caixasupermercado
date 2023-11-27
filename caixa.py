# Nesse projeto será criado um simulador de caixa de supermercado simples sem DB, usaremos apenas python simples.

produtoevalor = {"arroz": 5.50, "feijao": 4.50, "oleo": 8.00, "macarrao": 3.75}

produto = ""

contador = 0

carrinho = []

valor = []

total = []

quantiitens = [] 

while True:
   
   produto = input("Digite o nome do produto: ")
   
   
   if produto == "sair":
      break
   #Aqui o operador de caixa entra com quantidade, o valor do produto é salvo na lista valor pegando a chave do diciónario produtoevalor
   #O produto é add na lista carinnho, o total é add na lista total e quantiitens é uma lista que salvo a quantida de cada produto para saida do cupom fiscal
   else:
    quantidade = int(input("Digite a quantidade: "))
    valor = produtoevalor.get(produto)
    carrinho.extend([produto])
    total.append(quantidade * valor)
    quantiitens.append(quantidade)

    # Saida de atualização da compra para conferencia do cliente.
    print(f"{produto} x {produtoevalor[produto]} = {total[contador]}")
    print(f"TOTAL R$: {sum(total):.2f}")

    contador += 1

# Cabeçalho do Cupom fiscal
print("-" * 30)
print("SUPERMERCADO FANTASIA\n")
print("RUA INVENTÁRIO,BAIRRO: CENTRO, Nº 10\nSÂO JOSÉ- SC\n")
print("CNPJ: 89.455.000/003-00")
print("-" * 30)

# Corpo do cupom fiscal
print('CUPOM FISCAL\n')

print('CÓD QUANT ITEM. VALOR.\n')
# Laçor for para montagém do cupom fiscal
for c in range(0, len(quantiitens)):
  print(c + 1, quantiitens[c],  carrinho[c], total[c])

print("-" * 30, "\n")
print(f"TOTAL R$: {sum(total):.2f}")

#Rodapé do cupom fiscal para informações
print("-" * 30)
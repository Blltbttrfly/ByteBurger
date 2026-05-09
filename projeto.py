print("Bem vindo à hamburgueria ByteBurger!")
print()
itens = ["X-Burguer", "X-Salada", "Fritas", "Refrigerante", "Suco", "Sorvete"]
precos = [18.50, 21.00, 9.00, 6.50, 7.00, 8.00 ] 

nome_cliente = []
comanda_prod = []


while True:
    for i, nome in enumerate(itens):
        print(f"{i + 1}. {nome} ........ R$ {precos[i]:.2f}")


    nome_cliente = input("Digite o nome do cliente que aparecerá na comanda: ")
    if nome_cliente == "fim":
        break

    while True: 
        pedidos = int(input("Digite o numero do produto desejado: "))
        
        if pedidos == 0:
            break
        
        comanda_prod.append(pedidos) 

print([comanda_prod])
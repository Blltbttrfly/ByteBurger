
itens = ["X-Burguer", "X-Salada", "Fritas", "Refrigerante", "Suco", "Sorvete"]
precos = [18.50, 21.00, 9.00, 6.50, 7.00, 8.00 ] 

clientes = []
total_faturamento = []


while True:
    print("Bem vindo à hamburgueria ByteBurger!")
    print()
    for i, nome in enumerate(itens):
        print(f"{i + 1}. {nome} ........ R$ {precos[i]:.2f}")

    print()

    item_cliente = [] # Etapa 2 
    valor_pedido = []


    cliente = input("Digite o nome do cliente que aparecerá na comanda: ")
    clientes.append(cliente)
    if cliente == "fim":
        break

    while True: 
        pedidos = int(input("Digite o numero do produto desejado: "))
        
        if pedidos == 0:
            break
        item_cliente.append(itens[pedidos-1])
        valor_pedido.append(precos[pedidos-1])

        
    print(f"COMANDA DE {cliente}") # Etapa 5 
    for j, p in enumerate(item_cliente):
        print(f"{j+1} - {p} ........... R$ {valor_pedido[j]:.2f}")
        print(f"Total: R$ {sum(valor_pedido):.2f}")

        total_faturamento += precos[pedidos-1]

    acabar = input("Finalizar o pedido?: ")
    if acabar.upper == "FIM":
        break

print(f"""
Número de clientes atendidos: 
{len(clientes)}
""")    
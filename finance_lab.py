nome = input("Digite seu nome: ")
dinheiro = float(input("Digite seu dinheiro: "))
produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
produto_buy = dinheiro - preco
if dinheiro >= 0 and preco > 0:
    print("=== RELATÓRIO FINANCEIRO ===")
    print(f"Produto: {produto}")
    print(f"Preço: {preco:.2f}")
    print(f"Saldo inicial: {dinheiro:.2f}")

    if dinheiro > preco:
        print("Compra possivel")
        print(f"Saldo restante: {produto_buy:.2f}")
    elif dinheiro == preco:
        print("Compra possível sem saldo restante ")

    else:
        print("Dinheiro insuficiente")
        print(f"Saldo necessario: {preco - dinheiro:.2f}")

else:
    print("Dados inválidos")


    



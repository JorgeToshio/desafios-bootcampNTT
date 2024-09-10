#Desafio banco

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True: #Para rodar até o break
    opcao = input(menu).lower() #Chaman
    if opcao == "d":
        valor = float(input("Informe o valor do depósito R$ "))
        if valor >0:
            saldo +=valor
            extrato += f"Depósito de R$ {valor:.2f}\n" 
        else:
            print("Informe valor acima de R$ 0.00 e tente novamente!")
    elif opcao =="s":
        valor = float(input("Informe o valor do saque R$ "))# Estou lendo um valor através do imput e armazenando na variável
        valor_acima_saldo = valor > saldo #Teste boleano, resulta true or false
        valor_acima_limite = valor > limite #Teste boleano, resulta true or false
        qtd_acima_saques = numero_saques >= limite_saques #Teste boleano, resulta true or false
        if valor_acima_saldo:
            print(f"Valor de tentativa do saque R$ {valor:.2f} acima do saldo em conta R$ {saldo:.2f}!")
        elif valor_acima_limite:
            print(f"Valor de tentativa do saque R$ {valor:.2f} excede o limite R$ {limite:.2f}!")
        elif qtd_acima_saques:
            print(f"Quantidade de {limite_saques} saques excedido")
        elif valor > 0 :
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque realizado de R${valor:.2f}")
        
        else:
            print(f"Operação inválida")
    elif opcao=="e":
        print("\n ================Extrato================")
        print("\n Sem movimentações"if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("\n =======================================")
    elif opcao =="q":
        print(f"Saindo do sistema.....")
        break
    else:
        print("Operação invalida, por gentileza selecione operação válida!")




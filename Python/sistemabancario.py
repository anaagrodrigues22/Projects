saldo = 0

menu = """   
    Escolha uma opçao:

    [d] Depósito
    [s] Saque
    [e] Extrato
    [q] Sair

"""

print(menu)

qnt =0
depositos=[]
saques=[]
while True:
    opcao=input(menu)
    
    if opcao == 'd':
        depo = int(input("Digite o valor do deposito: "))

        while depo < 0:
            print("Não é possivel realizar o deposito")
            depo = int(input("Digite o valor do deposito: "))
            
        saldo = saldo + depo
        dep = "R$"+str(depo)
        depositos.append(dep)
    elif opcao == 's':
        saque = int(input("Digite o valor do saque: "))
    
        while saque < 0:
            print("Não é possivel realizar um deposito negativo")
            saque = int(input("Digite o valor do saque: "))
        
        while saque > saldo:
            print("Seu saldo não é suficiente")
            saque = int(input("Digite o valor do saque: "))
        
        while saque > 500:
            print("Não é permitido sacar mais de 500 reais por saque")
            saque = int(input("Digite o valor do saque: "))
        
        qnt = qnt + 1
        if qnt <= 3:
            saq = "R$"+str(saque)
            saques.append(saq)
            saldo = saldo - saque  
        else:
            print("Seu limite de saque diario foi atingido (3)")
        
    elif opcao == 'e':
        if len(depositos) == 0:
            if len(saques) == 0:
                print("Nao houve movimentacoes nesta conta")
            print("saques:",saques, "saldo: R$ ",saldo)
            break
        if len(saques) == 0:
            print("saldo: R$ ", saldo)
            print("Depositos",depositos)
            break

        print("saque:",saques, "depositos:",depositos, "\nsaldo: R$ ",saldo)

    elif opcao == 'q':
        break


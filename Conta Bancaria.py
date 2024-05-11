menu = """
O que deseja realizar?

1 - Depósito

2 - Saque

3 - Extrato

4 - Sair

Opção Escolhida: 

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input (menu)
    
    if opcao == "1":
        valor = float(input("\nInforme o valor de depósito: \n"))
        
        if valor > 0:
            saldo += valor
            extrato += f"""\nDepósito: R$ {valor:.2f}\n"""
            
            print ('''\nDepósito de R$ {} realizado com sucesso!'''.format(valor))
        
        else:
            print ("""
                   Valor inválido
                   
                   Escolha um valor maior que R$ 0""")
            
    elif opcao == "2":
        valor = float(input("\nInforme o valor de saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print ("\nSaldo Insuficiente")
            
        elif excedeu_limite:
            print ("\nValor maior que o limite")
            
        elif excedeu_saques:
            print ("\nNúmero de saque diário excedido")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"\nSaque: R$ {valor:.2f}\n"
            numero_saques += 1
            
        else:
            print ("\nValor inválido")
        
    elif opcao == "3":
        print ("\n===================EXTRATO========================")
        print ("Não foram realizadas movimentações em sua conta" if not extrato else extrato)
        print (f"\nSaldo: R$ {saldo:.2f}")
        print ("\n==================================================")
        
    elif opcao == "4":
        break
    
    else:
        print ("\nOperação inválida, escolha uma das opções a seguir:")
saldo = 0
while True:
    opcao = int(input(
'''Bem vindo ao Banco AmoJava  
1 - Sacar dinheiro       
2 - Depositar dinheiro   
3 - Ver saldo            
4 - Sair   
Escolha uma opção: '''))

    if(opcao == 1):
        saque = float(input("Digite o valor para saque: "))
        if(saldo < saque):
            print("Saldo insuficiente para saque!")
        else:
            saldo = saldo - saque
            print(f"Saque realizado! Seu saldo atual é R$ {saldo}")

    elif(opcao == 2):
        deposito = float(input("Digite o valor para depósito: "))
        saldo += deposito
        print(f"Depósito realizado! Seu saldo atual é: R$ {saldo}")

    elif(opcao == 3):
        print(f"Seu saldo atual é: R$ {saldo}")

    elif(opcao == 4):
        print("Obrigada por usar o banco AmoJava :)")
        break
    else:
        print("Digite uma opção válida!")

    
    

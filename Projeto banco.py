nome = input(("Olá digite seu nome: "))
print(f"olá, {nome}")

    
menu= """"
Digite o número da opção desejada:   
 
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Quanto você vai depositar?: "))
            
        if valor > 0:
            saldo += valor
            extrato += f" Você fez um Depósito de R$ {valor: .2f} "
        else:
            print("o valor digitado não é válido")    
    
    elif opcao == "2" :
        valor = float(input("Quanto você vai sacar?: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Você não tem esse valor na conta para sacar")
            
        elif excedeu_limite:
            print("Esse valor é maior que seu limite de saque")
        
        elif excedeu_saques:
            print("Esse valor é maior que seu limite de saque")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de {valor: .2f} efetuado!\n"
            numero_saques += 1
        
        else :
            print("Valor inválido")
                
    elif opcao == "3" :
       
       print("\n////////////////////// EXTRATO //////////////////////")   
       print("você não fez nenhum saque e nenhum depósito" if not extrato else extrato)
       print(f"\n Seu Saldo é de: R$ {saldo: .2f}")
       print("/*/*/*/*/*/*/**/**/*/*/*/*/*/**/*/*/*/*/*/*/*/*/*/*/*/*/")
    
    elif opcao == "4":
        break
    
    else:
        print("Algo deu errado. Vamos tentar novamete! digite a opção desejada: ")   
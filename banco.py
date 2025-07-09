valorTotal = 500
limiteSaques = 3
acao = -1 
extrato = "" 

while acao != 0: 
    acao = int(input("""
Boa tarde, o que você deseja fazer hoje?
========================================
[1] Depósito
[2] Saque
[3] Extrato
[0] Sair                
    
"""))

    if acao == 1:
        valorDeposito = float(input("Quanto voce gostaria de depositar? "))
        if valorDeposito < 0:
            print("Valor Inválido")
        else:
            valorTotal += valorDeposito
            print("Foi depositado {valor}".format(valor=valorDeposito))
            extrato += f"Deposito: R${valorDeposito:.2f} \n"


    if acao == 2 and limiteSaques != 0:
        limiteSaques -= 1
        if limiteSaques == 0:
            print("Limite de saques atingidos")

        valorSaque = float(input("Quanto voce gostaria de sacar? "))
        if valorSaque < 0:
            print("Valor Inválido")
        elif valorSaque > valorTotal:
            print("Saldo insuficiente")
        elif valorSaque > 500:
            print("Valor acima do permitido")
        else:
            valorTotal -= valorSaque
            extrato += f"Saque: R${valorSaque:.2f} \n"


    if acao == 3:
        print("Transições feitas:")
        print(extrato)
        print("Valor disponível {valor}".format(valor=valorTotal))

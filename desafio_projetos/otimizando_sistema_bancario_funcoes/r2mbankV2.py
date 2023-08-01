# R2M Bank

start = '''
====== R2M Bank ======

[1] - DEPOSITAR
[2] - SACAR
[3] - EXTRATO
[0] - SAIR

======================
'''

exit_msg = "Obrigado por utilizar nosso sistema, volte sempre!"

saldo = 0
extrato = f""
numero_saques = 0
LIMITE_QTD_SAQUE = 3
LIMITE_VALOR_SAQUE = 500

def depositar(saldo, valor, extrato, /,):
    if valor <= 0:
            print("OPERAÇÃO INVÁLIDA")
            print("O valor de depósito precisar ser positivo!")
    else:
        saldo += valor
        extrato = extrato + f"DEPÓSITO => + R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
        return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques == limite_saques:
            print(f"Saque indisponível - Seu limite diário de saques por dia é apenas {limite_saques} saques.")  
    elif valor > limite:
            print(f"Saque indisponível - Seu valor limite por saque é de R$ {limite:.2f}")
    else:
        if valor <= saldo:
            numero_saques += 1
            saldo -= valor
            extrato = extrato + f"SAQUE => - R$ {valor:.2f}\n"
            print("Saque realizado com sucesso!")
            return saldo, extrato
        else:
            print("Saldo insuficiente!")

    
#   return saldo, extrato


def ver_extrato(saldo, /, *, extrato):
    print("====================== EXTRATO ==============================")
    print(f"{extrato}")
    print(f"SALDO ATUAL => R$ {saldo:.2f}")
    print("=============================================================")
    input("Pressione ENTER voltar ao menu inicial!")


while True:
    print(start)
    choice = str(input("Favor selecione a opção desejada: "))
    if choice not in ['0','1','2','3']:
        print("Opção inválida!".upper().center(21))
        continue

    # SAIR
    if choice == "0":
        print(exit_msg)
        break


    # DEPOSITAR
    elif choice == "1":
        value = float(input("Digite o valor do despósito a realizar: R$ ").replace(",","."))
        deposito = depositar(saldo, value, extrato)
        if deposito != None:
            saldo = deposito[0]
            extrato = deposito[1]


    # SACAR
    elif choice == "2":
        value = float(input("Digite o valor do saque a realizar: R$ ").replace(",","."))
        saque = sacar(saldo=saldo, valor=value, extrato=extrato, limite=LIMITE_VALOR_SAQUE, numero_saques=numero_saques, limite_saques=LIMITE_QTD_SAQUE)
        if saque != None:
            saldo = saque[0]
            extrato = saque[1]
            numero_saques += 1
    

    # EXTRATO
    elif choice == "3":
        ver_extrato(saldo, extrato=extrato)

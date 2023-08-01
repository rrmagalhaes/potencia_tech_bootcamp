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
        if value <= 0:
            print("OPERAÇÃO INVÁLIDA")
            print("O valor de depósito precisar ser positivo!")
            continue
        else:
            saldo += value
            extrato = extrato + f"\nDEPÓSITO => + R$ {value:.2f}"
            print("Depósito realizado com sucesso!")

    # SACAR
    elif choice == "2":
        value = float(input("Digite o valor do saque a realizar: R$ ").replace(",","."))
        if numero_saques == LIMITE_QTD_SAQUE:
            print(f"Saque indisponível - Seu limite diário de saques por dia é apenas {LIMITE_QTD_SAQUE} saques.")
            continue
        elif value > LIMITE_VALOR_SAQUE:
            print(f"Saque indisponível - Seu valor limite por saque é de R$ {LIMITE_VALOR_SAQUE:.2f}")
        else:
            if value <= saldo:
                numero_saques += 1
                saldo -= value
                extrato = extrato + f"\nSAQUE => - R$ {value:.2f}"
                print("Saque realizado com sucesso!")
            else:
                print("O valor solicitado é maior que o saldo disponível em conta.")
                continue



    # EXTRATO
    elif choice == "3":
        print(f'''
        {extrato}

        SALDO ATUAL => R$ {saldo:.2f}
        ''')
        input("Pressione ENTER voltar ao menu inicial!")

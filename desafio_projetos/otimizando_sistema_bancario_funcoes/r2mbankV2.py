# R2M Bank

start = '''
====== R2M Bank ======

[1] - DEPOSITAR
[2] - SACAR
[3] - EXTRATO
[4] - CADASTRAR CLIENTE
[5] - LISTAR CLIENTES
[6] - CRIAR CONTA
[0] - SAIR

======================
'''

exit_msg = "Obrigado por utilizar nosso sistema, volte sempre!"

saldo = 0
extrato = f""
numero_saques = 0
LIMITE_QTD_SAQUE = 3
LIMITE_VALOR_SAQUE = 500
clientes = []
contas = []

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


def ver_extrato(saldo, /, *, extrato):
    print("====================== EXTRATO ==============================")
    print(f"{extrato}")
    print(f"SALDO ATUAL => R$ {saldo:.2f}")
    print("=============================================================")
    input("Pressione ENTER voltar ao menu inicial!")


def existe_cliente(cpf, clientes):
    for cli in clientes:
        if cpf in cli:
            existe = True
            #print("Cliente já encontrado!")
            break    
        else:
            existe = False
            #print("Cliente não encontrado!")
    
    return existe


def solicitar_dados(cpf):
    print("Para realizar o cadastro, digite as informações conforme solicitado.")

    nome = input("NOME COMPLETO: ").upper()
    data_nascimento = input("DATA DE NASCIMENTO: ")

    logradouro = input("LOGRADOURO (RUA/AV/TRAV): ").upper()
    numero = input("NÚMERO: ")
    bairro = input("BAIRRO: ").upper()
    cidade = input("CIDADE: ").upper()
    uf = input("UF: ").upper()

    endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{uf}"

    cliente = { cpf : {"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco }}

    return cliente
     

def criar_cliente(clientes):
    cpf = input("CPF: ")
    if clientes == []:
        dados = solicitar_dados(cpf)
        clientes.append(dados)
        return 'Cliente Cadastrado com Sucesso'
    else:
        existe = existe_cliente(cpf, clientes)
        if existe == False:
            dados = solicitar_dados(cpf)
            clientes.append(dados)
            return 'Cliente Cadastrado com Sucesso'
        

def listar_clientes(clientes):
    if clientes != []:
        for cli in clientes:
            data = list(cli.items())
            print(f"Nome: {data[0][1]['nome']:50} CPF: {data[0][0]:20} Endereço: {data[0][1]['endereco']:130} ")
    else:
        print("Não existe clientes cadastrados.")


def criar_conta(cpf, contas):
    AGENCIA = "0001"
    total_contas = len(contas)
    numero_conta = str(total_contas + 1)
    conta = {"agencia": AGENCIA, "numero": numero_conta, "cpf_titular": cpf}
    return conta


#'''
while True:
    print(start)
    choice = str(input("Favor selecione a opção desejada: "))
    if choice not in ['0','1','2','3','4','5','6']:
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


    # CADASTRAR CLIENTE
    elif choice == "4":
        cadastro = criar_cliente(clientes)
        if cadastro != None:
            print(cadastro)
        else:
            print("Cadastro não permitido, o CPF já existe em nossa base!")

    
    # LISTAR CLIENTES
    elif choice == "5":
        print("LISTA DE CLIENTES".center(200, '-') + "\n")
        listar_clientes(clientes)
        print("-" * 200)

    # CRIAR CONTA
    elif choice == '6':
        cpf = input("Insira o CPF para qual deseja abrir a conta: ")
        if clientes == []:
            print("Cliente não cadastrado na base de dados.")
        else:
            existe = existe_cliente(cpf, clientes)
            if existe == False:
                print("Cliente não cadastrado na base de dados.")
            else:
                conta = criar_conta(cpf, contas)
                contas.append(conta)
                print(f"Conta número {conta['numero']} criada.")
#'''
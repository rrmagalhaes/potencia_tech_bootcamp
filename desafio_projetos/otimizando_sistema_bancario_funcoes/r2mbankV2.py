# R2M Bank

start = '''
====== R2M Bank ======

[1] - DEPOSITAR
[2] - SACAR
[3] - EXTRATO
[4] - CADASTRAR CLIENTE
[5] - LISTAR CLIENTES
[6] - CRIAR CONTA
[7] - LISTAR CONTAS
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
# Usado em testes
#clientes = [{ '027' : {"nome": 'Renato', "data_nascimento": '26', "endereco": 'Rua do seu zé' }}, { '033' : {"nome": 'Camila', "data_nascimento": '26', "endereco": 'Rua do seu zé' }}]

contas = []

def depositar(saldo, valor, extrato, /,):    
    """Função responsável por realizar a operação de depósito

    Args:
        saldo (float): Valor existente em conta
        valor (float): Valor que será depositado
        extrato (str): Acumula mensagens referentes as operações

    Returns:
        str: saldo e extrato
    """
    if valor <= 0:
            print("OPERAÇÃO INVÁLIDA")
            print("O valor de depósito precisar ser positivo!")
    else:
        saldo += valor
        extrato = extrato + f"DEPÓSITO => + R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
        return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """Função responsável por realizar a operação de saque

    Args:
        saldo (float): Valor existente em conta
        valor (float): Valor que será sacado
        extrato (str): Acumula mensagens referentes as operações
        limite (float): Valor financeiro máximo permitido para saque
        numero_saques (int): Quantidade de saques realizados
        limite_saques (int): Quantidade limite de saques permitidos

    Returns:
        str: saldo e extrato
    """
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
    """Fançao responsável por exibir as informações de extrato bancário

    Args:
        saldo (float): Valor existente em conta
        extrato (str): Acumula mensagens referentes as operações
    """
    print("====================== EXTRATO ==============================")
    print(f"{extrato}")
    print(f"SALDO ATUAL => R$ {saldo:.2f}")
    print("=============================================================")
    input("Pressione ENTER voltar ao menu inicial!")


def existe_cliente(cpf, clientes):
    """Valida a existência do clientes atráves do "cpf" repassado na lista "clientes".

    Args:
        cpf (str): CPF do cliente a consultar
        clientes (list): Lista com as informações do clientes cadastrados

    Returns:
        bool: Retorna o valor booleano da verificação
    """
    for cli in clientes:
        if cpf in cli:
            existe = True
            #print("Cliente já encontrado!")
            break    
        else:
            existe = False
            #print("Cliente não encontrado!")
    
    return existe


def nome_cliente(cpf, clientes=clientes):
    """Funação responsável por retornar o nome do cliente em relação ao "cpf" repassado e consultado na lista "clientes".

    Args:
        cpf (str): CPF do cliente a consultar
        clientes (list): Lista com as informações do clientes cadastrados

    Returns:
        str: Retorna o nome do cliente, caso seja encontrado.
    """
    if clientes != []:
        for cli in clientes:                  
            data = list(cli.items())
            cpf_cli = data[0][0]
            if cpf == cpf_cli:
                return data[0][1]['nome']
        
        print("Não existe cadastro pro cpf solicitado.")
    else:
        print("Não existe clientes cadastrados.")  


def solicitar_dados(cpf):
    """Função responsável por solicitar as informações do cliente para cadastro.

    Args:
        cpf (str): CPF do cliente a consultar

    Returns:
        dict: Retorna um dicionário com as informações coletadas em tela
    """
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
    """Função responsável por realizar o cadastro do cliente na lista "clientes" utilizando o cpf como chave única.

    Args:
        clientes (list): Lista com as informações do clientes cadastrados

    Returns:
        str: Retorna mensagem de confirmação do cadastro quando assim ocorrer.
    """
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
    """Função responsável por listar os clientes repassados na lista "clientes".

    Args:
        clientes (list): Lista com as informações do clientes cadastrados

    Returns:
        str: Retorna todos os clientes cadastrado na lista "clientes" com a informação de Nome, CPF e Endereço
    """
    if clientes != []:
        for cli in clientes:
            data = list(cli.items())
            print(f"Nome: {data[0][1]['nome']:50} CPF: {data[0][0]:20} Endereço: {data[0][1]['endereco']:130} ")
    else:
        print("Não existe clientes cadastrados.")


def criar_conta(cpf, contas):
    """Função responsável por organizar as informações em uma dict para futura criação de conta.

    Args:
        cpf (str): CPF do cliente que será o titular da conta
        clientes (list): Lista com as informações do clientes cadastrados

    Returns:
        dict: Retorna um dicionário com os dados da conta queserá criada.
    """
    AGENCIA = "0001"
    total_contas = len(contas)
    numero_conta = str(total_contas + 1)
    conta = {"agencia": AGENCIA, "numero": numero_conta, "cpf_titular": cpf}
    return conta


def listar_contas(contas):
    """Função responsável por listar as contas repassadas na lista "contas".

    Args:
        contas (list): Lista com as informações das contas cadastrados

    Returns:
        str: Retorna todos as contas cadastrado na lista "contas" com a informação de Número da conta, agência, cpf do titular e também do nome do titular.
    """
    if contas != []:
        for conta in contas:            
            data = list(conta.items())
            cpf_cli = data[2][1]
            nome_cli = nome_cliente(cpf_cli)
            print(f"Número da conta: {data[1][1]:5} Agência: {data[0][1]:5} CPF do titular: {data[2][1]:12} Nome do titular: {nome_cli:50}")
    else:
        print("Não existem contas cadastradas.")



#'''
while True:
    print(start)
    choice = str(input("Favor selecione a opção desejada: "))
    if choice not in ['0','1','2','3','4','5','6','7']:
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


    # LISTAR CONTAS
    elif choice == "7":
        print("LISTA DE CONTAS".center(100, '-') + "\n")
        listar_contas(contas)
        print("-" * 100)
#'''
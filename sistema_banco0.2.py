
menu = """
[r] Criar conta corrente
[c] Criar Usuário
[d] Depositar
[s] Sacar
[e] Extrato
[lc] listar contas
[q] Sair

=> """

valor = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []


def criar_usuario(nome, data_de_nascimento, cpf, endereco, usuarios):
    cpf_numeros = ""
    for caractere in cpf:
        if caractere.isdigit():
            cpf_numeros += f"{caractere}"
    dicionario_usuarios = {"nome": nome, "data_de_nascimento": data_de_nascimento, "cpf": cpf_numeros, "endereco": endereco}
    usuario_encontrado = filtrar_usuarios(cpf_numeros, usuarios)
    if usuario_encontrado != None:
        return None
    else:
        usuarios.append(dicionario_usuarios)
        print("Usuário criado com sucesso!")
        return dicionario_usuarios

def criar_conta_corrente(cpf, usuario, contas):
    cpf_numeros = ""
    for caractere in cpf:
        if caractere.isdigit():
            cpf_numeros += f"{caractere}"
    usuario_encontrado = filtrar_usuarios(cpf_numeros, usuarios)
    if usuario_encontrado == None:
        print("CPF informado não foi encontrado")
        return None
    else:
        numero_da_conta = len(contas) + 1
        agencia = "0001"
        dicionario_contas = {"agencia": agencia, "numero da conta": numero_da_conta, "usuario": usuario_encontrado}
        contas.append(dicionario_contas)
        print(f"numero da conta: {numero_da_conta}")
        return dicionario_contas




def filtrar_usuarios(cpf_numeros, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf_numeros: # verifica se existe um CPF igual no dicionario usuários
            print(f'O cpf {usuario["cpf"]} já foi cadastrado no sistema')
            return usuario
    else:
        return None

def deposito(saldo, valor,extrato,/):

    if valor > 0:
        saldo += valor
        extrato += f"Depóstito: R${valor:.2f}\n"
        return saldo, extrato
    else:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato

def saque(*,saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        return saldo, extrato, numero_saques

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
        return saldo, extrato, numero_saques

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        return saldo, extrato, numero_saques

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}"
        numero_saques += 1
        return saldo, extrato, numero_saques

    else:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")



while True:

    opcao = input(menu).lower()

    if opcao == "c":
        nome = input("Digite seu Nome: ")
        data_de_nascimento = input("Digite sua data de nascimento: ")
        cpf = input("Digite seu CPF: ")
        endereco = input("Digite seu endereço: (logradouro, numero, bairro, cidade/sigla do estado): ")
        criar_usuario(nome, data_de_nascimento, cpf, endereco, usuarios)

    elif opcao == "r":
        cpf = input("Digite o CPF: ")
        criar_conta_corrente(cpf, usuarios, contas)

    elif opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo,valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: "))
        saldo, extrato, numero_saques = saque(saldo=saldo,valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "lc":
        for conta in contas:
            print(f"Agência: {conta["agencia"]}")
            print(f"C/C: {conta["numero da conta"]}")
            print(f"titular: {conta["usuario"]["nome"]}")
            print("=================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
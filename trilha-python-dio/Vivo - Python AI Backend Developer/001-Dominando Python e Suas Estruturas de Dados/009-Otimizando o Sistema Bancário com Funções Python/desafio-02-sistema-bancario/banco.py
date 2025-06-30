import textwrap

def menu():
    menu = """\n
    ===============<MENU>===============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    ⇒ """
    return input(textwrap.dedent(menu))


def depositar(saldo,valor,extrato,/):
    if(valor > 0):
        saldo +=valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato

def sacar(*,saldo,valor,extrato,limite,numero_saque,limite_saque):
    exedeu_saldo = valor > saldo
    exedeu_limite = valor > limite
    excedeu_saques = numero_saque >= limite_saque
    if exedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif exedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saque += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    print("\n================<EXTRATO>================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(usuario)
    print(f"\n@@@ Usuário {nome} cadastrado com sucesso! @@@")

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia,numero_conta,usuarios,contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf,usuarios)
    if not usuario:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
        return
    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    contas.append(conta)
    print(f"\n@@@ Conta de {usuario['nome']} criada com sucesso! @@@")
    return

def listar_contas(contas):
    if not contas:
        print("\n@@@ Não existem contas cadastradas. @@@")
        return
    for conta in contas:
        linha = f"Agência:\t{conta['agencia']}\n" \
                f"Número da conta:\t{conta['numero_conta']}\n" \
                f"Titular:\t{conta['usuario']['nome']}\n"
        print("=" * 40)
        print(linha)
    print("=" * 40)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    tentativas = 3

    while True:
        opcao = menu()
        if(opcao == "d"):
            valor = float(input("Informe o valor de depósito: "))
            saldo, extrato = depositar(saldo,valor,extrato)
        
        elif(opcao == "s"):
            valor = float(input("Inform o valor de saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                extrato=extrato,
                valor=valor,
                limite=limite,
                numero_saque=numero_saques,
                limite_saque=LIMITE_SAQUES
            )
        
        elif(opcao == "e"):
            exibir_extrato(saldo, extrato=extrato)
        
        elif(opcao == "nu"):
            criar_usuario(usuarios)
        
        elif(opcao == "nc"):
            numero_conta = len(contas)+1
            criar_conta(AGENCIA,numero_conta,usuarios,contas)

        elif(opcao == "lc"):
            listar_contas(contas)
        
        elif(opcao == "q"):
            break
        else:
            if tentativas > 0:
                print("Operação inválida, selecione novamente uma das operações.")
                tentativas -= 1
            else:
                print("Opção inválida, saindo do sistema.")
                break

main()

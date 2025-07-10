import textwrap
from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        if conta in self.contas:
            transacao.registrar(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, cliente, numero, agencia="0001"):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero, agencia="0001"):
        return cls(cliente, numero, agencia)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de {valor} realizado com sucesso. Saldo atual: {self.saldo}.")
            return True
        else:
            print("Valor de depósito inválido. O valor deve ser positivo.")
        
        return False

    def sacar(self, valor):
        saldo = self.saldo
        exedeu_saldo = valor > saldo

        if exedeu_saldo:
            print(f"Saldo insuficiente para saque de {valor}. Saldo atual: {saldo}.")
        elif valor > 0:
            self._saldo -= valor
            print(f"Saque de {valor} realizado com sucesso. Saldo atual: {self.saldo}.")
            return True
        else:
            print("Valor de saque inválido. O valor deve ser positivo.")

        return False

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, agencia="0001", limite=1000.0, limite_saques=3):
        super().__init__(cliente, numero, agencia)
        self._limite = limite
        self._limite_saques = limite_saques
    
    def sacar(self, valor):
        numero_saques = 0
        for transacao in self.historico.transacoes:
            if transacao["tipo"] == Saque.__name__:
                numero_saques += 1
        
        execedeu_limite = valor > self._limite
        execedeu_limite_saques = numero_saques >= self._limite_saques

        if execedeu_limite:
            print(f"Valor de saque {valor} excede o limite de {self._limite}.")
        elif execedeu_limite_saques:
            print(f"Número máximo de saques ({self._limite_saques}) já foi atingido.")
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"Conta Corrente {self.numero} - Agência {self.agencia} - Cliente: {self.cliente.nome}"

class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "data": datetime.now(),
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor
        })

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)
            print(f"Depósito de {self.valor} registrado na conta {conta.numero}.")
        else:
            print(f"Falha ao registrar depósito de {self.valor} na conta {conta.numero}.")

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)
            print(f"Saque de {self.valor} registrado na conta {conta.numero}.")
        else:
            print(f"Falha ao registrar saque de {self.valor} na conta {conta.numero}.")


def menu():
    menu = """
    ===============<MENU>===============
    [d]	Depositar
    [s]	Sacar
    [e]	Extrato
    [nc]	Nova conta
    [lc]	Listar contas
    [nu]	Novo cliente
    [q]	Sair
    ⇒ """
    return input(textwrap.dedent(menu))

def depositar(clientes):
    executar_transacao(clientes,"Informe o valor de depósito: ",Deposito)

def sacar(clientes):
    executar_transacao(clientes,"Informe o valor do saque: ",Saque)

def executar_transacao(clientes,msg,tipo_transacao):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf,clientes)
    if not cliente:
        print("\n@@@@ Cliente não encontrado @@@@")
        return
    
    valor = float(input(msg))
    transacao = tipo_transacao(valor)
    conta = recuperar_conta(cliente)

    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf,clientes)
    if not cliente:
        print("\n@@@@ Cliente não encontrado @@@@")
        return
    
    conta = recuperar_conta(cliente)
    if not conta:
        return
    
    print("\n@@@@====================== EXTRATO ======================@@@@")
    transacoes = conta.historico.transacoes
    
    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"
    
    print(extrato)
    print(f"\nSaldo: \n\tR$ {conta.saldo:.2f}")
    print("\n@@@@=====================================================@@@@")

def criar_cliente(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf,clientes)
    if cliente:
        print("\n@@@@ Já existe um cliente com esse CPF @@@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa)")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/uf):")

    cliente = PessoaFisica(nome=nome,cpf=cpf,data_nascimento=data_nascimento,endereco=endereco)
    clientes.append(cliente)
    print("\n@@@@ Cliente criado com sucesso! @@@@")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf,clientes)
    if not cliente:
        print("\n@@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@@")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente,numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n@@@@ Conta criada com sucesso! @@@@")

def listar_contas(contas):
    if not contas:
        print("\n@@@@ Nenhuma conta foi criada @@@@")
    for conta in contas:
        print("="*100)
        print(textwrap.dedent(str(conta)))

def filtrar_cliente(cpf, clientes):
    cliente = [cliente for cliente in clientes if cliente.cpf == cpf]
    return cliente[0] if cliente else None

def recuperar_conta(cliente):
    if not cliente.contas:
        print("\n@@@@ Cliente não possui conta! @@@@")
        return
    
    # FIXME: não permitir cliente escolher a conta
    return cliente.contas[0]


def main():
    clientes = []
    contas = []
    while True:
        opacao = menu()

        if opacao == 'd':
            depositar(clientes)
        elif opacao == 's':
            sacar(clientes)
        elif opacao == 'e':
            exibir_extrato(clientes)
        elif opacao == 'nu':
            criar_cliente(clientes)
        elif opacao == 'nc':
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opacao == 'lc':
            listar_contas(contas)
        elif opacao == 'q':
            break
        else:
            print("\n@@@@ Opecação inválida, por favor selecione novamente a operação desejada.")

main()
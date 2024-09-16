class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)


class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        conta.historico.adicionar_transacao(transacao)
        transacao.registrar(conta)

    def listar_contas(self):
        print(f"\nCliente: {self.nome} (CPF: {self.cpf})")
        if self.contas:
            for conta in self.contas:
                print(f"  - Conta {conta.numero} (Agência: {conta.agencia}) | Saldo: R$ {conta.saldo:.2f}")
        else:
            print("  - Nenhuma conta cadastrada.")


class Conta:
    def __init__(self, numero, agencia, cliente):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def saldo(self):
        return self.saldo

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
            return False
        else:
            self.saldo -= valor
            print(f"Saque de {valor} realizado")
            return True

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de {valor} realizado")
            return True
        else:
            print("Valor inválido")
            return False


class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente, limite, limite_saques):
        super().__init__(numero, agencia, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0

    def sacar(self, valor):
        if self.numero_saques >= self.limite_saques:
            print("Limite de saques excedido")
            return False
        elif valor > (self.saldo + self.limite):
            print("Saldo insuficiente, incluindo o limite")
            return False
        else:
            self.saldo -= valor
            self.numero_saques += 1
            print(f"Saque de {valor} realizado")
            return True


class Transacao:
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)


# Menu
clientes = []
contas = []

def cadastrar_cliente():
    nome = input("Nome: ")
    data_nascimento = input("Data de Nascimento: ")
    cpf = input("CPF: ")
    endereco = input("Endereço: ")

    if any(cliente.cpf == cpf for cliente in clientes):
        print("Erro: Já existe um cliente com esse CPF.")
    else:
        cliente = Cliente(nome, data_nascimento, cpf, endereco)
        clientes.append(cliente)
        print("Cliente cadastrado com sucesso!")


def cadastrar_conta():
    cpf = input("CPF do cliente: ")
    cliente = next((cliente for cliente in clientes if cliente.cpf == cpf), None)

    if cliente:
        numero_conta = len(contas) + 1
        conta = ContaCorrente(numero_conta, "0001", cliente, limite=500, limite_saques=3)
        cliente.adicionar_conta(conta)
        contas.append(conta)
        print("Conta cadastrada com sucesso!")
    else:
        print("Erro: Cliente não encontrado.")


def realizar_saque():
    numero_conta = int(input("Número da conta: "))
    valor = float(input("Valor do saque: "))
    conta = next((conta for conta in contas if conta.numero == numero_conta), None)

    if conta:
        saque = Saque(valor)
        saque.registrar(conta)
    else:
        print("Conta não encontrada.")


def realizar_deposito():
    numero_conta = int(input("Número da conta: "))
    valor = float(input("Valor do depósito: "))
    conta = next((conta for conta in contas if conta.numero == numero_conta), None)

    if conta:
        deposito = Deposito(valor)
        deposito.registrar(conta)
    else:
        print("Conta não encontrada.")


def exibir_extrato():
    numero_conta = int(input("Número da conta: "))
    conta = next((conta for conta in contas if conta.numero == numero_conta), None)

    if conta:
        print("\n================ EXTRATO ================")
        for transacao in conta.historico.transacoes:
            print(f"Transação: {transacao.__class__.__name__}, Valor: {transacao.valor}")
        print(f"Saldo: R$ {conta.saldo:.2f}")
        print("==========================================")
    else:
        print("Conta não encontrada.")


def listar_clientes():
    if clientes:
        for cliente in clientes:
            cliente.listar_contas()
    else:
        print("Nenhum cliente cadastrado.")


def menu():
    while True:
        print("\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[n] Novo Cliente\n[c] Nova Conta\n[l] Listar Clientes e Contas\n[q] Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "d":
            realizar_deposito()
        elif opcao == "s":
            realizar_saque()
        elif opcao == "e":
            exibir_extrato()
        elif opcao == "n":
            cadastrar_cliente()
        elif opcao == "c":
            cadastrar_conta()
        elif opcao == "l":
            listar_clientes()
        elif opcao == "q":
            break
        else:
            print("Opção inválida, tente novamente.")

# Inicia o menu
menu()

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.extrato = []

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.append(f"Depósito: +{valor}")
        print(f"Depósito de {valor} realizado com sucesso")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: -{valor}")
            print(f"Saque de {valor} realizado com sucesso")

    def mostrar_extrato(self):
        print(f"Extrato de {self.titular}")
        for transacao in self.extrato:
            print(transacao)
        print(f"Saldo Atual de {self.saldo}")

# Criando um objeto da classe ContaBancaria
minha_conta = ContaBancaria("Rômulo Zirbes", 1000)
minha_conta.mostrar_extrato()

# Realizando operações
minha_conta.depositar(500)
minha_conta.sacar(200)
minha_conta.mostrar_extrato()
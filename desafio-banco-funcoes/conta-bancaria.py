def cadastrar_usuario(usuarios, nome, data_nascimento, cpf, endereco):
    # Verifica se o CPF já está cadastrado
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Erro: Já existe um usuário com esse CPF.")
    else:
        usuario = {
            'nome': nome,
            'data_nascimento': data_nascimento,
            'cpf': cpf,
            'endereco': endereco
        }
        usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")

def cadastrar_conta(contas, usuarios, cpf):
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)
    if usuario:
        numero_conta = len(contas) + 1
        conta = {
            'agencia': '0001',
            'numero_conta': numero_conta,
            'usuario': usuario,
            'saldo': 0,
            'extrato': [],
            'limite': 500,
            'numero_saques': 0,
            'limite_saques': 3
        }
        contas.append(conta)
        print("Conta cadastrada com sucesso!")
    else:
        print("Erro: Usuário não encontrado.")

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    return saldo, extrato

def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    else:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in extrato:
            print(movimento)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Exemplos de uso
usuarios = []
contas = []

# Cadastro de um usuário
cadastrar_usuario(usuarios, "João Silva", "01/01/1990", "12345678900", "Rua A, 123 - Centro - Cidade/UF")

# Cadastro de uma conta
cadastrar_conta(contas, usuarios, "12345678900")

# Operações bancárias
conta = contas[0]

# Depósito
saldo_atualizado, extrato_atualizado = depositar(conta['saldo'], 100, conta['extrato'])
conta['saldo'] = saldo_atualizado
conta['extrato'] = extrato_atualizado

# Saque
saldo_atualizado, extrato_atualizado = sacar(saldo=conta['saldo'], valor=50, extrato=conta['extrato'], 
                                             limite=conta['limite'], numero_saques=conta['numero_saques'], 
                                             limite_saques=conta['limite_saques'])
conta['saldo'] = saldo_atualizado
conta['extrato'] = extrato_atualizado

# Exibir Extrato
exibir_extrato(conta['saldo'], extrato=conta['extrato'])

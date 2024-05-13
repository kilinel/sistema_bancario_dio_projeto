import textwrap

def menu():
    menu = """\n
    =============== MENU ===============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [du]\tDados do usuário
    [q]\tSair

    => """
    return input(textwrap.dedent(menu))


def saque(*,limite_saques, limite, saldo, valor, extrato, numero_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def deposito(saldo,valor,extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
         print("Operação falhou! O valor informado é inválido.")
    return saldo,extrato


def mostrar_extrato(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def formatar_cpf(cpf):
       
    cpf = ''.join(filter(str.isdigit, cpf))
        
       
    if len(cpf) == 11:
            
        cpf_formatado = '{}{}{}.{}{}{}.{}{}{}-{}{}'.format(*cpf)
        return cpf_formatado
    else:
        print("CPF inválido. Por favor, insira um CPF com 11 digitos.")
        return None

   




def criar_usuario(usuarios):
    #cpf = input("Informe o CPF(somente número): ")
   
    cpf_formatado = None
    while not cpf_formatado:
        cpf = input("Informe o CPF(somente número): ")
        cpf_formatado = formatar_cpf(cpf)
        print("CPF formatado:", cpf_formatado)  

    usuario = filtrar_usuario(cpf,usuarios)
    print("Usuário encontrado:", usuario) 

    if usuario:
        print("Usuário com esse CPF já existe no sistema")
        return
    
    nome = input("Informe o Nome completo: ")
    data_nascimento = input("Informe a data de nascimento(dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

   # novo_usuario = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}
    #usuarios.append(novo_usuario)
    return {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}
    


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    print("Usuários filtrados:", usuarios_filtrados)  
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF(somente número): ")
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
        print(" Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
     
    print("\n Usuario não encontrado, fluxo de criação encerrado")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))



def ver_usuario(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF(somente número): ")
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
        print("=" * 100)
        linha = f"""\
            Nome: {usuario['nome']}
            Data de Nascimento: {usuario['data_nascimento']}
            CPF: {usuario['cpf']}
            Endereço: {usuario['endereco']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
        return
     
    print("\n Usuario não encontrado, fluxo de criação encerrado")




def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    usuarios = []
    contas = []

    saldo = 0.0
    limite = 500
    extrato = ""
    numero_saques = 0
    numero_conta = 1

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = deposito(saldo,valor,extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            mostrar_extrato(saldo,extrato=extrato)
        elif opcao == "nu":
            usuario = criar_usuario(usuarios)
            
            if usuario:
                usuarios.append(usuario)
                print(usuarios)
        elif opcao == "nc":
            #numero_conta = len(contas) + 1

            conta = criar_conta(AGENCIA,numero_conta,usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

          
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "du":
            ver_usuario(AGENCIA,numero_conta,usuarios)
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")



main()
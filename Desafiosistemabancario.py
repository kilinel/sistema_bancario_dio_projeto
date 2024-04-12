
#Banco
#Depósito
#Saque
#Extrato


#Dep
# depositar valores positivos para a conta
# 1 usuario, sem numero de agencia e conta bancaria
# armazenados em 1 variavel e exibidos na operação de extrato

#Saque
#deve permitir realizar 3 saques diarios com limite maximo de 500 reais por saque
#caso ele não tenha o saldo, o sistema deve exibir uma msg informando sobre
#todos os saques devem ser armazenados em uma variavel e exibidos na operação de extrato

#Operação de extrato
# deve listar os depositos e saques da conta. no fim o saldo atual da conta
# devem ser exibidos no formato R$ xxxx.xx

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair


"""

from datetime import datetime


data_e_hora_atuais = datetime.now()

data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M:%S")

print(f"Dia Atual: {data_e_hora_em_texto}")

saldo = 0
limite = 500
extrato = ""

numero_saques = 0
numero_depositos = 0

LIMITE_SAQUES = 3
LIMITE_QUANTIA_SAQUE = 500

simbolo = "R$"


def mostrar_extrato():
    linha_extrato = "Extrato"
    newstring = linha_extrato.center(25,"=")
    print(f"\n{newstring}")
    print("Sem movimentações." if not extrato else f"{extrato} \n Número de Depósitos: {numero_depositos} \n Número de Saques: {numero_saques} \n Saldo Atual: {simbolo} {saldo:.2f}")
    linha_extrato = "="
    newstring = linha_extrato.center(25,"=")
    print(newstring)
    



while True:


    opcao = input(menu)

    if opcao == "1" or opcao.lower() == "depositar":
        print("Depósito")
        deposito = input("\nQual o valor que deseja depositar? : ")
        if float(deposito):
            if float(deposito) > 0 and float(deposito) != 0:
                 print(f"\nDepositando :  {simbolo} {float(deposito):.2f} ...")
                 numero_depositos += 1
                 data_e_hora_atuais = datetime.now()
                 data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M:%S") 
                 extrato = extrato + f"{numero_depositos}º Depósito :" + f"{simbolo} {float(deposito):.2f} Data: {data_e_hora_em_texto}" + "\n"

                 saldo += float(deposito)
                 print(f"Saldo : {simbolo} {saldo:.2f}")
            else:
                print("Operação inválida: use apenas números positivos.")
        else:
            print("Operação Inválida: use apenas números.")
    elif opcao == "2" or opcao.lower() == "sacar":
        print("Saque")
        saque = input("\nQual o valor que deseja sacar? : ")
        if float(saque):
            if float(saque) > 0 and float(saque) != 0:
                 if float(saque) <= saldo:
                     if numero_saques < LIMITE_SAQUES:
                         if float(saque) <= LIMITE_QUANTIA_SAQUE:
                            print(f"\nSacando :  {simbolo} {float(saque):.2f} ...")
                            saldo -= float(saque)
                            print(f"Saldo : {simbolo} {saldo:.2f}")
                            numero_saques += 1
                            print(f"Saques feitos: {numero_saques}")
                            print(f"Limite de Saques: {LIMITE_SAQUES}")
                            data_e_hora_atuais = datetime.now()
                            data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M:%S") 

                            extrato = extrato + f"{numero_saques}º Saque :" + f"{simbolo} {float(saque):.2f} Data: {data_e_hora_em_texto}" + "\n"
                         else:
                             print("Limite de saques excedido, tente novamente amanhã.")
                        
                     else:
                         print("Limite de saques excedido, tente novamente amanhã.")

                 else:
                    print("Operação Inválida: você não tem essa quantia depositada no banco.")

            else:
                print("Operação inválida: use apenas números positivos.")
        else:
            print("Operação Inválida: use apenas números.")


    elif opcao == "3" or opcao.lower() == "extrato":
        print("Extrato")
        mostrar_extrato()

    elif opcao == "4" or opcao.lower() == "sair":
        print("Saindo...")
        break
    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")
    



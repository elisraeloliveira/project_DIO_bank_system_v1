menu = """

[d]Depositar
[s]Sacar
[e]Extrato
[q]Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Informe o valor de deposito: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito: R${deposito:.2f}\n"

        else:
            print(f"Operação falhou! O valor informado é invalido.")


    elif opcao == "s":
        saque = float(input("Informe o valor de saque: "))

        excedeu_saldo = saque > saldo

        excedeu_limite = saque > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor de saque excede o limite para saques\n O seu limite para saque é R$ 500.")

        elif excedeu_saques:
            print("Operação falhou! Número de saques excedido")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$: {saque:.2f}"
            numero_saques += 1

        else:
            print("Operação falhou: O valor informado é inválido")


    elif opcao == "e":
        print("\n#################> EXTRATO <#################")
        print("Não houve movimentaçõa em sua conta." if not extrato else extrato)
        print(f"\n Saldo: R$: {saldo:.2f}")
        print("##############################################")




    elif opcao == "q":
        print("Obrigado por usar nossos serviços.")
        break

    else:
        print("Operação invalida, selecione por favor a opção desejada.")






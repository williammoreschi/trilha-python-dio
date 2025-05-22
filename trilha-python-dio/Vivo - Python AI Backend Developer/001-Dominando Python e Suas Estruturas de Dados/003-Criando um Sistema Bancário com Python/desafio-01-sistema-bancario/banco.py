menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite= 500
numero_saque = 0
LIMITE_SAQUE = 3
tentativas = 3
extrato = []

while True:
    opcao = str(input(menu)).lower()[0]

    if opcao == "d":
        print("Opção Depositar")
        while True:
            valor = str(input("Digite o valor: ")).strip()
            try:
                valor_convertido = float(valor)

                if valor_convertido <= 0:
                    print("Valor inválido, digite um valor positivo.")
                    continue

                saldo += valor_convertido
                extrato.append(f"Deposito: R$ {valor_convertido:.2f}\n")
                print(f"\033[34mDeposito de R$ {valor_convertido:.2f} realiza do com sucesso\033[m")
                print("\033[34mSeu Dinheiro já está rendendo, com nosso CDB de 300% do CDI! 😀\033[m")
                break
            except ValueError:
                print("\033[0;31mErro! Digite um valor válido.\033[m")

    elif opcao == "s":
        print("Opção Sacar")
        if numero_saque == LIMITE_SAQUE:
            print("\033[33mLimite diário de saque em caixa atingido, para novos saques dirir-se ao banção\033[m")
        else:
            while True:
                valor = str(input("Digite o valor: ")).strip()
                try:
                    valor_convertido = float(valor)
                    if valor_convertido <= 0:
                        print("Valor inválido, digite um valor positivo.")
                    elif(valor_convertido > saldo):
                        print("\033[33mSaldo Insuficiente.\033[m")
                        break
                    elif(valor_convertido > limite):
                        print(f"\033[33mValor ultrapassa o limite diário que é de R$ {limite:.2f}\033[m")
                    else:
                        saldo -= valor_convertido
                        extrato.append(f"Saque: R$ {valor_convertido:.2f}\n")
                        numero_saque += 1
                        print(f"\033[34mSaque de R$ {valor_convertido:.2f} realiza do com sucesso\033[m")
                    break
                except ValueError:
                    print("\033[0;31mErro! Digite um valor válido.\033[m")

    elif opcao == "e":
        print("-*"*20)
        if extrato:
            for key, value in enumerate(extrato):
                print(f"{key+1} > {value} ")
            print(f"Saldo: R$ {saldo:.2f}")
        else:
            print("Nenhuma operação foi realizada")
        print("-*"*20)
    elif opcao == "q":
        print("Obrigado por usar nosso banco. Até logo!")
        break
    else:
        if tentativas > 0:
            print("Opção inválida, por favor selecione a operação desejada.")
            tentativas -= 1
        else:
            print("Opção inválida, saindo do sistema.")
            break

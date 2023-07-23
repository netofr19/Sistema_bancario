# Definicao do menu
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
historico_depositos = []
historico_saques = []

print("Sistema Bancário")
print("--------------------------")
print("Menu de opções")
print("[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair")
print("--------------------------")
print("\n")

while True:

    opcao = input("Por favor, digite uma opção: ")
    opcao = opcao.lower()
    print("\n")

    if opcao == "d":
        print("Você selecionou a opção 'DEPÓSITO'")
        valor_deposito = input("Por favor, digite o valor para depósito: ")
        valor_deposito = float(valor_deposito)
        if valor_deposito > 0:
            saldo += valor_deposito
            historico_depositos.append(valor_deposito)
            print("Depósito realizado com sucesso!")
            print(f"Seu saldo agora é: R$ {saldo:.2f}")
        else:
            print("Operação Inválida! O valor informado está incorreto!")
        print("\n")

    elif opcao == "s":
        print("Você selecionou a opção 'SAQUE'")
        valor_saque = input("Por favor, digite o valor para saque: ")
        valor_saque = float(valor_saque)
        if valor_saque <= limite and numero_saques < LIMITE_SAQUES:
            if valor_saque <= saldo:
                saldo -= valor_saque
                numero_saques += 1
                historico_saques.append(valor_saque)
                print("Saque realizado com sucesso!")
            else:
                print("Saque não autorizado! O valor solicitado para saque é maior do que seu saldo.")
        elif valor_saque <= limite and numero_saques >= LIMITE_SAQUES:
            print("Saque não autorizado! Você atingiu seu limite de saques diários.")
        elif valor_saque > limite and numero_saques < LIMITE_SAQUES:
            print("Saque não autorizado! Você excedeu o valor máximo para saque.")
        else:
            print("Saque não autorizado! Por favor, entre em contato com o seu gerente!")
        print("\n")

    elif opcao == "e":
        print("Você selecionou a opção 'EXTRATO'")
        if len(historico_depositos) == 0 and len(historico_saques) == 0:
            print("Não foram realizadas movimentações nesta conta.")
        else:
            print("Histórico de depósitos:")
            for i, j in enumerate(historico_depositos):
                print(f"Depósito {i+1:.0f} = R$ {j:.2f}")
            print("\n")
            print("Histórico de saques:")
            for i, j in enumerate(historico_saques):
                print(f"Saque {i+1:.0f} = R$ {j:.2f}")
            print("\n")
            print(f"SALDO ATUAL = R$ {saldo:.2f}")
        print("\n")

    elif opcao == "q":
        break

    else:
        print("Opção inválida! Por favor, selecione uma opção válida.")
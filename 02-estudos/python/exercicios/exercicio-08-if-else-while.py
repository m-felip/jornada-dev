# Exercício

# Crie um programa que simule um caixa eletrônico.
# O programa deve:

# Começar com um saldo:
# saldo = 1000

# Mostrar um menu:
# 1 - Consultar saldo
# 2 - Sacar dinheiro
# 3 - Sair

# Enquanto o usuário não escolher sair:

# Se escolher 1:
# mostrar saldo atual.

# Se escolher 2:
# perguntar o valor do saque.
# diminuir do saldo.

# Se escolher 3:
#  encerrar o programa.

#while (colinha)
    # mostra menu
    # recebe opção
    # if opção == 1
    # elif opção == 2
    # elif opção == 3
    # else

# Resposta:

saldo = 1000

opcao = 0

while opcao != 3:

    print("\n=== CAIXA ELETRÔNICO ===")
    print("1 - Consultar saldo")
    print("2 - Sacar dinheiro")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print(f"Seu saldo é R${saldo}")

    elif opcao == 2:
        saque = float(input("Digite o valor do saque: "))

        if saque <= saldo:
            saldo -= saque
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente.")

    elif opcao == 3:
        print("Sistema encerrado.")

    else:
        print("Opção inválida.")

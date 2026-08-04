# Desafio: FINAL BOSS:

# Crie um Sistema de Caixa/Atendimento simples no terminal:

# Programa

usuario = input("Digite o nome do usuário: ")

print(f"Bem vindo ao Mercado Dev, {usuario}!")

numero1 = 545
numero2 = 320
opcao = 0

print(f"Aqui, realizaremos operações, simulando um caixa interativo com estes números: {numero1} e {numero2}")

while opcao != 5:

    print("\n=== CAIXA INTERATIVO ===")
    print("1 - Somar valores")
    print("2 - Verificar maior número")
    print("3 - Calcular média")
    print("4 - Contar de 1 até um número")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        soma = numero1 + numero2
        print(f"A soma é:{soma}.")

    elif opcao == 2:
        if numero1 > numero2:
            print(f"O número {numero1} é o maior.")
        else: 
            print(f"O número {numero2} é o maior")
      
    elif opcao == 3:
        media = (numero1 + numero2) / 2
        print(f"A média dos dois números é:{media}")

    elif opcao == 4:
        for numero3 in range(1,6):
            print(numero3)

    else:
        print("Programa encerrado.")

# Exercício

# Crie um programa que:

# Pergunte ao usuário quantos números ele deseja somar.
# Enquanto ainda não tiver atingido essa quantidade:
# peça um número;
# some esse número em uma variável acumuladora.
# Ao final, mostre a soma total.

# Resposta

quantidade = int(input("Quantos números deseja somar? "))
soma = 0
contador = 1

while contador <= quantidade:
    numero = int(input("Digite um número: "))
    soma += numero
    contador += 1
print(f"A soma total foi: {soma}")

# Explicação:

# Pergunta ao usuário quantos números ele quer somar
# Essa informação vai definir quantas vezes o nosso loop vai rodar
quantidade = int(input("Quantos números deseja somar? "))


# ACUMULADOR
# Essa variável começa em 0 porque ainda não temos nenhum valor somado
# Ela vai guardando o resultado da soma a cada repetição
soma = 0


# CONTADOR
# Essa variável controla quantas vezes o loop já aconteceu
# Começamos em 1 porque vamos contar a primeira entrada de número como a primeira repetição
contador = 1


# Enquanto o contador ainda não chegou na quantidade desejada,
# o programa continua repetindo
while contador <= quantidade:


    # Pede um número para o usuário a cada repetição do loop
    numero = int(input("Digite um número: "))


    # ACUMULADOR EM AÇÃO
    # Pega o valor que já estava guardado em "soma"
    # e adiciona o novo número informado pelo usuário
    #
    # Exemplo:
    # soma = 0
    # usuário digita 5
    # soma vira 0 + 5 = 5
    #
    # usuário digita 10
    # soma vira 5 + 10 = 15
    soma += numero


    # CONTADOR EM AÇÃO
    # Aumenta o contador em 1 para avisar que uma repetição terminou
    #
    # Exemplo:
    # contador = 1 → primeira nota/número
    # contador = 2 → segunda nota/número
    # contador = 3 → terceira nota/número
    contador += 1


# Quando o loop termina, significa que já recebemos todos os números
# Então mostramos o resultado final que ficou guardado no acumulador
print(f"A soma total foi: {soma}")

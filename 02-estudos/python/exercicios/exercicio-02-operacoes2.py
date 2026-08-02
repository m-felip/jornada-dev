#EXERCÍCIO

#Crie um programa que:

#Pergunte o nome do usuário;
#Pergunte dois números;
#Calcule:
#Soma;
#Subtração;
#Multiplicação;
#Divisão;
#Mostre o nome do usuário;
#Mostre todos os resultados identificados.

#RESPOSTA

nome = input("Digite seu nome: ")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print(f"Olá, {nome}! Seguem os resultados conforme solicitado: ")
print(f"Soma: {soma}, Subtração: {subtracao}, Multiplicação: {multiplicacao} e Divisão: {divisao}")
# EXERCÍCIO

# Crie um programa que:

# 1. Pergunte o nome do usuário;
# 2. Pergunte o primeiro número;
# 3. Pergunte o segundo número;
# 4. Calcule a soma;
# 5. Calcule a subtração;
# 6. Calcule a multiplicação;
# 7. Mostre uma mensagem com o nome do usuário;
# 8. Mostre os três resultados de forma identificada.

# RESPOSTA

nome = input("Digite seu nome: ")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

print(f"Olá, {nome}!")
print(f"A soma é: {soma}")
print(f"A subtração é: {subtracao}")
print(f"A multiplicação é: {multiplicacao}")

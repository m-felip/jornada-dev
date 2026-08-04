# Exercício

# Criar um programa que:

# Pergunte ao usuário se deseja continuar (sim ou nao).
# Enquanto ele responder “sim”:
# Mostre: Programa executando...
# Pergunte novamente se deseja continuar.
# Quando responder “nao”, mostre: Programa encerrado.

# Resposta

programa = input("Deseja continuar? (sim/não) ")

while programa == "sim":
    print("Programa executando...")
    programa = input("Deseja continuar? (sim/não) ")

print("Programa encerrado.")


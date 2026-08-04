# Exercício

# Criar um programa que simule o fechamento das notas de uma turma.
# O programa deve:
# Perguntar quantos alunos existem na turma.
# Utilizar for para repetir essa quantidade de vezes.
# Para cada aluno:
# pedir a nota;
# somar todas as notas.
# Ao final:
# mostrar a soma das notas;
# calcular a média;
# informar se a turma foi aprovada.

# Regra
# Se a média for maior ou igual a 7:
# Turma aprovada!

# Caso contrário:
# Turma em recuperação.

# Resposta

soma = 0
quantidade = int(input("Digite a quantidade de alunos: "))

for aluno in range(1, quantidade + 1):
    nota = float(input("Digite a nota do aluno: "))
    soma += nota

print(f"A soma das notas é: {soma}")

media = soma / quantidade

print(f"A média das notas é: {media}")
if media >= 7:
    print("Turma aprovada!")
else:
    print("Turma em recuperação.")


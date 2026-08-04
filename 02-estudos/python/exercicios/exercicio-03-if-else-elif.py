# Exercício

# Crie um programa que:

# Pergunte o nome do aluno;
# Pergunte a nota da primeira prova;
# Pergunte a nota da segunda prova;
# Calcule a média das duas notas;
# Verifique a situação do aluno:
# Média >= 7 → Aprovado
# Média >= 5 → Recuperação
# Média < 5 → Reprovado
# Mostre o nome do aluno;
# Mostre a média;
# Mostre a situação final.

# Resposta

nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
media = (nota1 + nota2) / 2
situacao = " "

if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"Olá, {nome}! Sua média é {media}, e sua situação final é {situacao}!")


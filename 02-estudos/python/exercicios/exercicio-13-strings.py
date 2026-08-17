# Exercício

# Crie um programa que faça o cadastro de uma pessoa e trate os textos digitados pelo usuário antes de exibi-los.
# Quero que você tente resolver usando o que já estudamos até agora, principalmente Strings, mas misturando conceitos das aulas anteriores.

# O usuário deverá informar:

# Nome:
# Cidade:
# Profissão:
# Linguagem favorita:

# O problema é que nosso usuário é um animal e pode digitar coisas assim:

# Nome:       matheus felipe
# Cidade:     JUIZ DE FORA
# Profissão:      gestor de pessoas
# Linguagem favorita: PYTHON

# Regras
# Nome: remova espaços das extremidades e deixe as iniciais maiúsculas.
# Cidade: remova espaços e deixe as iniciais maiúsculas.
# Profissão: remova espaços e deixe as iniciais maiúsculas.
# Linguagem favorita: remova espaços e transforme tudo em minúsculas para fazer uma comparação.
# Se a linguagem informada for "python", mostre: Excelente escolha!
# Caso contrário: Boa escolha! Continue estudando.

# No final, mostre uma ficha parecida com:

# ========== CADASTRO DEV ==========
# Nome: Matheus Felipe
# Cidade: Juiz De Fora
# Profissão: Gestor De Pessoas
# Linguagem favorita: Python

# Cadastro realizado com sucesso!

# Resposta

nome = input("Nome: ")
cidade = input("Cidade: ")
profissao = input("Profissão: ")
linguagem = input("Linguagem favorita: ")

nome = nome.strip().title()
cidade = cidade.strip().title()
profissao = profissao.strip().title()
linguagem = linguagem.strip().upper()

print(f"\n========== CADASTRO DEV ==========")
print(f"Nome: {nome}")
print(f"Cidade: {cidade}")
print(f"Profissão: {profissao}")
print(f"Linguagem favorita: {linguagem}")

if linguagem == "PYTHON":
    print("Excelente escolha!")
else: 
    print("Boa escolha, continue estudando.")

print(len(nome))
print(len(cidade))
print(len(profissao))
print(len(linguagem))

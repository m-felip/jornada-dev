# Exercício

# Crie um programa que peça:
# Nome de usuário
# Senha

# Considere que os dados corretos são:
# usuario_correto = "matheus"
# senha_correta = "python123"

# Regras

# 1. Remova os espaços das extremidades do usuário e da senha.

# 2. Faça o nome de usuário funcionar independentemente
# de letras maiúsculas ou minúsculas.
#
# Exemplos que devem funcionar:
# MATHEUS
# Matheus
# matheus

# 3. A senha deve ser comparada exatamente como foi digitada,
# removendo apenas os espaços das extremidades.
#
# Portanto:
# PYTHON123 é diferente de python123.

# 4. Se usuário e senha estiverem corretos, exiba:
# Login realizado com sucesso!

# 5. Se o usuário estiver correto, mas a senha estiver errada, exiba:
# Senha incorreta.

# 6. Se o usuário estiver errado, exiba:
# Usuário não encontrado.


# Bônus

# Se o login for realizado com sucesso, exiba também:
# Bem-vindo, Matheus!
# Sua senha possui 9 caracteres.


# Resposta

# Considere que os dados corretos são:
# usuario_correto = "matheus"
# senha_correta = "python123"

nome = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

nome = nome.strip().lower()
senha = senha.strip()

if nome == "matheus":
    if senha == "python123":
        print("Login realizado com sucesso! Bem vindo, Matheus! Sua senha possui 9 caracteres.")
    else: 
        print("Senha incorreta.")
else:
    print("Usuário não encontrado.")

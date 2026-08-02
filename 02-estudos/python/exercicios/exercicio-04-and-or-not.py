#EXERCÍCIO

#Criar um programa que:
#Verifica se uma pessoa pode acessar uma área restrita.

#O programa deverá perguntar:

#O nome da pessoa;
#A idade;
#Se ela possui autorização (sim ou nao);
#Se ela está bloqueada (sim ou nao).
#Regras de acesso:

#A pessoa poderá entrar somente se:

#Tiver 18 anos ou mais;
#E possuir autorização;
#E NÃO estiver bloqueada.

#RESPOSTA

#Cadastro:

pessoa = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
autorizacao = input("Possui autorização? (sim/nao): ")
bloqueado = input("A pessoa está bloqueada? (sim/nao): ")

#Regras de acesso:

if idade >= 18 and autorizacao == "sim" and not bloqueado == "sim":
    print("Você poderá acessar a área restrita")
else:
    print("Você não poderá acessar a área restrita")

# Exercício

# Crie uma biblioteca, com menu interativo e seguindo as seguintes regras:

# Crie uma lista vazia chamada livros.
# Na opção 1, pergunte o nome do livro e adicione com append().
# Na opção 2, percorra a lista com for e mostre todos os livros.
# Na opção 3, pergunte o nome do livro e remova com remove().
# Na opção 4, mostre quantos livros existem usando len().
# Na opção 5, encerre o programa.

# Você vai reutilizar while, if, for e input().

# Resposta

livros = [ ]
opcao = 0

while opcao != 5:

    print("\n=== Biblioteca Dev ===")
    print("1 - Adicionar livro")
    print("2 - Mostrar livros")
    print("3 - Remover livro")
    print("4 - Mostrar quantidade de livros")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        livro = input("Digite o nome de um livro: ")
        livros.append(livro)

    elif opcao == 2:
        for livro in livros:
            print(livro)

    elif opcao == 3:
        remover_livro = input("Qual livro você gostaria de remover? ")
        livros.remove(remover_livro)

    elif opcao == 4: 
        len(livros)
        print(len(livros))

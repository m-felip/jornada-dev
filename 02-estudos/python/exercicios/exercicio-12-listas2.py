# Exercício

# Criar um gerenciador de playlist.

# Opção 1 - Adicionar música
# Opção 2 - Mostrar playlist
# Opção 3 - Remover música
# Opção 4 - Pesquisar música
# Opção 5 - Mostrar quantidade
# Opção 6 - Sair


playlist = []
opcao = 0
contador = 0

while opcao != 6:

    print("\n========== PLAYLIST DEV ==========")
    print("1 - Adicionar música")
    print("2 - Mostrar playlist")
    print("3 - Remover música")
    print("4 - Pesquisar música")
    print("5 - Mostrar quantidade")
    print("6 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        musica = input("Adicione uma música: ")
        playlist.append(musica)

    elif opcao == 2:
        contador = 1
        for musica in playlist:
            print(musica)
            contador +=1

    elif opcao == 3:
        remover_musica = input("Remova uma música: ")
        playlist.remove(remover_musica)

    elif opcao == 4:
        pesquisar_musica = input("Digite a música que você queira pesquisar: ")
        if pesquisar_musica in playlist:
            print("Música encontrada")
        else: 
            print("Música não encontrada.")

    elif opcao == 5:
        print(len(playlist))

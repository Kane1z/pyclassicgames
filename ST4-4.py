tabuleiro = [[' ' for i in range(3)] for j in range(3)]

rondas = 0
jogador = 1
vencedor = None

while rondas < 9 and not vencedor:
    print("")
    for i in range(3):
        print(tabuleiro[i][0], '|', tabuleiro[i][1], '|', tabuleiro[i][2])
        print('-' * 10)

    print("Jogador", jogador)

    y = int(input("linha: ")) - 1
    x = int(input("coluna: ")) - 1
    if tabuleiro[y][x] == ' ':
        if jogador == 1:
            tabuleiro[y][x] = 'X'
            jogador = 2
        else:
            tabuleiro[y][x] = 'O'
            jogador = 1
        rondas += 1
    else:
        print("Posição já ocupada!")

    #  vamos ver se alguém foi habilidoso  para ganhar em horizontal +999QI...
    for i in range(3):
        if (tabuleiro[i][0] == tabuleiro[i][1]) and (tabuleiro[i][1] == tabuleiro[i][2]) and (tabuleiro[i][0] != ' '):
            vencedor = tabuleiro[i][0]
            break

    # Verificação vertical
    for i in range(3):
        if (tabuleiro[0][i] == tabuleiro[1][i]) and (tabuleiro[1][i] == tabuleiro[2][i]) and (tabuleiro[0][i] != ' '):
            vencedor = tabuleiro[0][i]
            break

    # A famosa jogada ninja a bruce lee na diagonal!
    if (tabuleiro[0][0] == tabuleiro[1][1]) and (tabuleiro[1][1] == tabuleiro[2][2]) and (tabuleiro[0][0] != ' '):
        vencedor = tabuleiro[0][0]
    if (tabuleiro[0][2] == tabuleiro[1][1]) and (tabuleiro[1][1] == tabuleiro[2][0]) and (tabuleiro[0][2] != ' '):
        vencedor = tabuleiro[0][2]

    if vencedor == 'X':
        print("Jogador 1 'X' venceu!")
    elif vencedor == 'O':
        print("Jogador 2 'O' venceu!")

for i in range(3):
    print(tabuleiro[i][0], '|', tabuleiro[i][1], '|', tabuleiro[i][2])
    print('-' * 10)

if not vencedor:
    print("Fim do jogo! Empate!")
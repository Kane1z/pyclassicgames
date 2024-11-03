# Código atualizado 21/10/24 -- 23:32
from ctypes.wintypes import tagMSG

TAM = 0
while True:
    TAM = int(input("Tamanho da grade (entre 5 e 10): "))
    if (5 <= TAM <= 10):
        break
    print("Valor inválido. Tente novamente.")

tabuleiro = [[' ' for i in range(TAM)] for j in range(TAM)]
turno = 1
plays = 0
ini = True
maxplay = (TAM * TAM) - TAM #maximo de jogada por tabulairo - o indicador (1-X)




while ini == True:
    print("max", maxplay)
    for linha in range(len(tabuleiro)):
        for coluna in range(TAM):
            if (linha == 0):
                print('|', coluna + 1, '', end='')
            else:
                print('|', tabuleiro[linha][coluna], '', end='')
        print('|')
    if(maxplay <= 0):
        print("jogo empatado")
        break
    print('-' * (4*TAM) + '-') # novo metodo mod para variar o tamanho
    # Código atualizado 22/10/24 -- 21:32 (atualizacao de turno)
    if (turno == 1):
        print("turno 1")
        coluna = int(input(f"Escolha uma coluna (1-{TAM}): ")) - 1
        char = 'X'

    else:
        print("turno 2")
        coluna = int(input(f"Escolha uma coluna (1-{TAM})): ")) - 1
        char = 'O'

    '''colocquei esse for que comeca na linha 5 ate 
          o final para verificar se há algo em baixo gostei bastante parece uma cascata'''
    if ( 0 <= coluna <= TAM):
        inserido = False
        #verificacao inversa de 0(base) ate tam-1 que o max do tabuleiro
        for linha in range((TAM-1), 0, -1):
            if (tabuleiro[linha][coluna] == ' '):
                tabuleiro[linha][coluna] = char
                inserido = True
                maxplay -= 1
                break
        if (inserido == False):
            print("Coluna cheia, escolha outra.")
        else:
            '''caso nao esteja cheia vai 
                ficar vareando entre turno 1 e 2'''
            if (turno == 1):
                turno = 2
            else:
                turno = 1

            # Código atualizado 23/10/24 -- 00:18 (atualizacao de verificacao de vencer)
            combobraker = 0
            '''muito basico vai fazer 2 verificacoes talvez ahaja repeticao de codigo mas... eh'''
            # Buffer overflow: quando o código decide que é hora de dar uma pausa mas eu não.
            for i in range(TAM):  # vericao horizontal
                if (tabuleiro[linha][i] == char):
                    combobraker += 1
                    if (combobraker == 4):
                        ini = False
                        if (char == 'X'):
                            print("Jogador 1 venceu yay!")
                        else:
                            print("Jogador 2 venceu yay!")
                        break
                else:
                    combobraker = 0
            if (ini == False):
                break

            combobraker = 0
            for i in range(TAM):  # verificacao vertical
                if (tabuleiro[i][coluna] == char):
                    combobraker += 1
                    if (combobraker == 4):
                        ini = False
                        if (char == 'X'):
                            print("Jogador 1 venceu!")
                        else:
                            print("Jogador 2 venceu!")
                        break
                else:
                    combobraker = 0


    else:
        print("Coluna não existe!")
#aquela repticao de codigo basica para mostrar o tabuleiro no final
for linha in range(len(tabuleiro)):
    for coluna in range(TAM):
        if (linha == 0):
            print('|', coluna + 1, '', end='')
        else:
            print('|', tabuleiro[linha][coluna], '', end='')
    print('|')
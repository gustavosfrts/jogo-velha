import random
import os

def verificadorCoordenada(string,matriz):
    #Verifica se coordenada é valida
    if(string[0] == 'a' or string[0] == 'b' or string[0] == 'c'):
        if(string [1] == '1' or string [1] == '2' or string [1] == '3'):
            coluna = int(conversao(string))
            linha = int(string[1])
            if(matriz[linha][coluna] == '_'):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

#realiza a conversão da Letra (no tabuleiro) para numero
def conversao(string):
    coluna = string[0]
    if(coluna == 'a'):
        coluna = '1'
        return coluna
    if(coluna == 'b'):
        coluna = '2'
        return coluna
    if(coluna == 'c'):
        coluna = '3'
        return coluna

#Realiza o registro de jogada do player no tabuleiro
def jogadaPlayer(matriz,coordenadas):
    coluna = int(conversao(coordenadas))
    linha = int(coordenadas[1])
    matriz[linha][coluna] = 'X'
    return matriz

#Realiza a jogada do bot no tabuleiro(de maneira aleatoria)
def jogadaBot(matriz):
    linha = random.randint(1,3)
    coluna = random.randint(1,3)
    
    while (matriz[linha][coluna] != '_' ):
        linha = random.randint(1,3)
        coluna = random.randint(1,3)
    
    matriz[linha][coluna] = 'O'
    return matriz

#Imprime o tabuleiro
def imprimirTabuleiro(matriz):
    i = 0
    while(i<4):
        i2 = 0
        while(i2 <4):
            if i2 == 3:
                print(matriz[i][i2])
            else:
                print(matriz[i][i2], end=' ')
            i2 += 1
        i += 1
    return 'Null'

def verificaVitoria(matriz):
    #VERIFICADOR VITORIA PLAYER
    #verifica coluna A - Player
    if(matriz[1][1] == 'X'):
        if(matriz[2][1] == 'X'):
            if(matriz[3][1] == 'X'):
                print("Parabéns você venceu do bot!.")
                return True
    #verifica coluna B - Player
    if(matriz[1][2] == 'X'):
        if(matriz[2][2] == 'X'):
            if(matriz[3][2] == 'X'):
                print("Parabéns você venceu do bot!.")
                return True
    #verifica coluna C - Player
    if(matriz[1][3] == 'X'):
        if(matriz[2][3] == 'X'):
            if(matriz[3][3] == 'X'):
                print("Parabéns você venceu do bot!.")
                return True    
    #verifica linha 1 - Player
    if(matriz[1][1] == 'X'):
        if(matriz[1][2] == 'X'):
            if(matriz[1][3] == 'X'):
                print("Parabéns você venceu do bot!.")
                return True
    #verifica linha 2 - Player
    if(matriz[2][1] == 'X'):
        if(matriz[2][2] == 'X'):
            if(matriz[2][3] == 'X'):
                print("Parabéns você venceu do bot!.")
                return True
    #verifica linha 3 - Player
    if(matriz[3][1] == 'X'):
        if(matriz[3][2] == 'X'):
            if(matriz[3][3] == 'X'):
                print("Parabéns você venceu do bot!.")
                return True
    #verifica diagonal A1 B2 C3 - Player
    if(matriz[1][1] == 'X'):
        if(matriz[2][2] == 'X'):
            if(matriz[3][3] == 'X'):
                print("Parabéns você venceu do bot!.")
                return True
    #verifica diagonal C1 B2 A3 - Player
    if(matriz[1][3] == 'X'):
        if(matriz[2][2] == 'X'):
            if(matriz[3][1] == 'X'):
                print("Parabéns você venceu do bot!.")
                return True

    #VERIFICADOR VITORIA BOT
    #verifica coluna A - Bot
    if(matriz[1][1] == 'O'):
        if(matriz[2][1] == 'O'):
            if(matriz[3][1] == 'O'):
                print("Infelizmente você perdeu para o bot! Tente novamente abrindo e fechando o jogo.")
                return True
    #verifica coluna B - Bot
    if(matriz[1][2] == 'O'):
        if(matriz[2][2] == 'O'):
            if(matriz[3][2] == 'O'):
                print("Infelizmente você perdeu para o bot! Tente novamente abrindo e fechando o jogo.")
                return True
    #verifica coluna C - Bot
    if(matriz[1][3] == 'O'):
        if(matriz[2][3] == 'O'):
            if(matriz[3][3] == 'O'):
                print("Infelizmente você perdeu para o bot! Tente novamente abrindo e fechando o jogo.")
                return True    
    #verifica linha 1 - Bot
    if(matriz[1][1] == 'O'):
        if(matriz[1][2] == 'O'):
            if(matriz[1][3] == 'O'):
                print("Infelizmente você perdeu para o bot! Tente novamente abrindo e fechando o jogo.")
                return True
    #verifica linha 2 - Bot
    if(matriz[2][1] == 'O'):
        if(matriz[2][2] == 'O'):
            if(matriz[2][3] == 'O'):
                print("Infelizmente você perdeu para o bot! Tente novamente abrindo e fechando o jogo.")
                return True
    #verifica linha 3 - Bot
    if(matriz[3][1] == 'O'):
        if(matriz[3][2] == 'O'):
            if(matriz[3][3] == 'O'):
                print("Infelizmente você perdeu para o bot! Tente novamente abrindo e fechando o jogo.")
                return True
    #verifica diagonal A1 B2 C3 - Bot
    if(matriz[1][1] == 'O'):
        if(matriz[2][2] == 'O'):
            if(matriz[3][3] == 'O'):
                print("Infelizmente você perdeu para o bot! Tente novamente abrindo e fechando o jogo.")
                return True
    #verifica diagonal C1 B2 A3 - Bot
    if(matriz[1][3] == 'O'):
        if(matriz[2][2] == 'O'):
            if(matriz[3][1] == 'O'):
                print("Infelizmente você perdeu para o bot! Tente novamente abrindo e fechando o jogo.")
                return True
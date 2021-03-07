import random
import os

def verificadorCoordenada(string):
    #Verifica se coordenada é valida
    if(string[0] == 'a' or string[0] == 'b' or string[0] == 'c'):
        if(string [1] == '1' or string [1] == '2' or string [1] == '3'):
            return True
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

def jogadaPlayer(matriz,coordenadas):
    coluna = int(conversao(coordenadas))
    linha = int(coordenadas[1])
    matriz[linha][coluna] = 'X'
    return matriz

def jogar(matriz):
    linha = random.randint(1,3)
    coluna = random.randint(1,3)
    
    while (matriz[linha][coluna] == '_' ):
        linha = random.randint(1,3)
        coluna = random.randint(1,3)
    
    matriz[linha][coluna] = 'O'

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
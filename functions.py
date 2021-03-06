import random

def verificadorCoordenada(string):
    #Verifica se coordenada é valida
    if(string[0] == 'a' or string[0] == 'b' or string[0] == 'c'):
        if(string [1] == '1' or string [1] == '2' or string [1] == '3'):
            return True
        else:
            return False
    else:
        return False
    
def verificadorJogada(string,matriz):
    #Verifica se coordenada está vazia
    linha = string[0]
    coluna = string[1]

    if(linha == 'a'):
        linha = 1
    if(linha == 'b'):
        linha = 2
    if(linha == 'c'):
        linha = 3
    
    if(matriz[linha][coluna] == '_'):
        matriz[linha][coluna] = 'X'
        return matriz
    else:
        return False


def jogar(matriz):
    linha = random.randint(1,3)
    coluna = random.randint(1,3)
    
    while (matriz[linha][coluna] == '_' ):
        linha = random.randint(1,3)
        coluna = random.randint(1,3)
    
    matriz[linha][coluna] = 'O'
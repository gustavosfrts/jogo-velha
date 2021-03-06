import random

def verificadorJogada(string):
    if(string[0] == 'a' or string[0] == 'b' or string[0] == 'c'):
        if(string [1] == '1' or string [1] == '2' or string [1] == '3'):
            return True
        else:
            return False
    else:
        return False

def jogar(matriz):
    linha = random.randint(1,3)
    coluna = random.randint(1,3)
    
    while (matriz[linha][coluna] == '_' ):
        linha = random.randint(1,3)
        coluna = random.randint(1,3)
    
    matriz[linha][coluna] = 'O'
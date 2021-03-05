import os

tabuleiro =[
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_']
]

print("Bem vindo ao Jogo da velha!")
ops = input("Informe qual modo você queira jogar:\n1- Contra Player\n2- Contra bot \n")

#Imprimir tabuleiro
""" i = 0
while(i<3):
    i2 = 0
    while(i2 <3):
        if i2 == 2:
            print(tabuleiro[i][i2])
        else:
            print(tabuleiro[i][i2], end=' ')
        i2 += 1
    i += 1
 """
os.system("pause")
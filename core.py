import os
import functions

tabuleiro =[
    [' ','A','B','C'],
    ['1','_','_','_'],
    ['2','_','_','_'],
    ['3','_','_','_']
]

print("Bem vindo ao Jogo da velha!")
print("Você no momento está jogando contra um bot! \n \n")

#opções para jogar
""" ops = int(input("Informe qual modo você queira jogar:\n1- Contra Player\n2- Contra bot \n"))

while (ops != 1 and ops != 2):
    ops = int(input("Opção incorreta! Por gentileza, informe novamente o modo que você queira jogar:\n1- Contra Player\n2- Contra bot \n"))

if(ops == 1):
    print("Teste")

if(ops == 2):
    print("Teste1") """

#Imprimir tabuleiro
i = 0
while(i<4):
    i2 = 0
    while(i2 <4):
        if i2 == 3:
            print(tabuleiro[i][i2])
        else:
            print(tabuleiro[i][i2], end=' ')
        i2 += 1
    i += 1

print("\n \n")

jogadaPlayer = input("Escolha as coordenadas onde deseja jogar:")
jogadaPlayer = jogadaPlayer.replace(" ","") #Retirar possiveis espaços da coordenada
jogadaPlayer = jogadaPlayer.lower() #Parametrizar as coordenadas

#Verifica se as coordenadas preenchidas pelo jogador é valida
while(functions.verificadorCoordenada(jogadaPlayer) == False):
    jogadaPlayer = input("Coordenadas incorretas! Por favor, preencha corretamente as coordenadas onde deseja jogar:")
    jogadaPlayer = jogadaPlayer.replace(" ","") #Retirar possiveis espaços da coordenada
    jogadaPlayer = jogadaPlayer.lower() #Parametrizar as coordenadas

#Verifica se a coordenada está vazio

os.system("pause")
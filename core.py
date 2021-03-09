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

contadorjogadas = 0

while(contadorjogadas < 9):
    #Imprimir tabuleiro
    functions.imprimirTabuleiro(tabuleiro)
    if(contadorjogadas % 2 == 0):    
        print("\n \n")
        jogadaPlayer = input("Escolha as coordenadas onde deseja jogar:")
        jogadaPlayer = jogadaPlayer.replace(" ","") #Retirar possiveis espaços da coordenada
        jogadaPlayer = jogadaPlayer.lower() #Parametrizar as coordenadas
        #Verifica se as coordenadas preenchidas pelo jogador é valida
        while(functions.verificadorCoordenada(jogadaPlayer,tabuleiro) == False):
            jogadaPlayer = input("Coordenadas incorretas! Por favor, preencha corretamente as coordenadas onde deseja jogar:")
            jogadaPlayer = jogadaPlayer.replace(" ","") #Retirar possiveis espaços da coordenada
            jogadaPlayer = jogadaPlayer.lower() #Parametrizar as coordenadas

        functions.jogadaPlayer(tabuleiro,jogadaPlayer) #Player joga
        print("\n")
        if(functions.verificaVitoria(tabuleiro)):
            functions.imprimirTabuleiro(tabuleiro)
            break
    else:
        functions.jogadaBot(tabuleiro) #Bot joga(de maneira completamente randomica, sem inteligencia)
        print("O bot está pensando no que jogar...")
        print("\n")
        if(functions.verificaVitoria(tabuleiro)):
            functions.imprimirTabuleiro(tabuleiro)
            break

    contadorjogadas += 1
    if(contadorjogadas == 9):
        functions.imprimirTabuleiro(tabuleiro)
        print("\nVelha!\n")

os.system("pause")
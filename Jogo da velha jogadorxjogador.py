import numpy as np

#criar o jogo da velha
#dois jogadores
#entrada jogador1
#matriz com entrada de string
#identificar posicoes
#regras do jogo
#use o seu teclado numero para jogar

teclado=np.array([[7,8,9],[4,5,6],[1,2,3]])
print(teclado)
print('O teclado numérico representa \nas posições de linhas e colunas')
print()

linha=3
coluna=3
matriz=np.array([['','',''],['','',''],['','','']])


def jogar(matriz,linha,coluna,jogador):
    matriz=matriz
    linha=linha
    coluna=coluna
    jogador=jogador
    contador=0
    
    for i in range(3):
        for j in range(3):
            if matriz[i][j]=='x' or matriz[i][j]=='0':
                contador=contador+1
                #kl=matriz[i][j]
                #lista[i][j]=(kl)
    
    if contador==9:
        print('Jogo encerrado')

    else:
   
        #print("As casas onde nao tem 'X' ou 'O' nao pode jogar")
        #print('Selecione a Linha e Coluna onde deseja jogar')
        matriz[linha][coluna]=jogador
        print('JOGO DA VELHA: \n',matriz)
        print()
        #zzzzzzzzzzzzzzzzzzzzverifica(matriz)

# verifica se tem algum vencedor
def verifica(matriz):
    matriz=matriz
    if matriz[0][0]==matriz[0][1]==matriz[0][2]!='':
        #print('caso 1')
        #print('Temos um vencedor')
        #print(matriz)
        caso=True
        return caso
    elif matriz[1][0]==matriz[1][1]==matriz[1][2]!='':
        #print('caso 2')
        #print('Temos um vencedor')
        #print(matriz)
        caso=True
        return caso
    
    elif matriz[2][0]==matriz[2][1]==matriz[2][2]!='':
        #print('caso 3')
        #print('Temos um vencedor')
        #print(matriz)
        caso=True
        return caso
    
    elif matriz[0][0]==matriz[1][0]==matriz[2][0]!='':
        #print('caso 4')
        #print('Temos um vencedor')
        #print(matriz)
        caso=True
        return caso
    
    elif matriz[0][1]==matriz[1][1]==matriz[2][1]!='':
        #print('caso 5')
        #print('Temos um vencedor')
        #print(matriz)
        caso=True
        return caso
    elif matriz[0][2]==matriz[1][2]==matriz[2][2]!='':
        #print('caso 6')
        #print('Temos um vencedor')
        #print(matriz)
        caso=True
        return caso
    elif matriz[0][0]==matriz[1][1]==matriz[2][2]!='':
        #print('caso 7')
        #print('Temos um vencedor')
        #print(matriz)
        caso=True
        return caso
    elif matriz[2][0]==matriz[1][1]==matriz[0][2]!='':
        #print('caso 8')
        #print('Temos um vencedor')
        #print(matriz)
        caso=True
        return caso
    else:
        caso=False
        #caso false, o jogo continua
        return caso

 # verifica se tem algum vencedor
print('Jogo da Velha: \n',matriz)
print()

def loop():
    teclado=[1,2,3,4,5,6,7,8,9]
    linhacoluna=0
    caso=False
    while caso==False:
        caso=verifica(matriz)  
        if caso==True:
        # caso haja algum vencedor, ele retorna verdadeira
            print('Temos um vencedor')
            break

#zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
                #zzzzzzzzzzzz   fase do jogador 1   zzzzzzzzzzzzzzzzzzzzzzzzz
            

        else: # caso o resultado de CASO seja false, entao:
            contador=0
            while contador==0:
                jogador='x'
                print('-------------JOGADOR X-------------')
                print("As casas onde tem 'X' ou '0' nao pode jogar")
                linhacoluna=int(input('Insira a posicao de acordo com o teclado: \n'))
                print()
                if linhacoluna==7:
                    linha=0
                    coluna=0
                    jogar(matriz,linha,coluna,jogador)

                elif linhacoluna==8:
                    linha=0
                    coluna=1
                    jogar(matriz,linha,coluna,jogador)

                elif linhacoluna==9:
                    linha=0
                    coluna=2
                    jogar(matriz,linha,coluna,jogador)

                elif linhacoluna==4:
                    linha=1
                    coluna=0
                    jogar(matriz,linha,coluna,jogador)
                
                elif linhacoluna==5:
                    linha=1
                    coluna=1
                    jogar(matriz,linha,coluna,jogador)
                
                elif linhacoluna==6:
                    linha=1
                    coluna=2
                    jogar(matriz,linha,coluna,jogador)

                elif linhacoluna==1:
                    linha=2
                    coluna=0
                    jogar(matriz,linha,coluna,jogador)

                elif linhacoluna==2:
                    linha=2
                    coluna=1
                    jogar(matriz,linha,coluna,jogador)

                elif linhacoluna==3:
                    linha=2
                    coluna=2
                    jogar(matriz,linha,coluna,jogador)
                else:
                    print('Vc precisa selecionar apenas com base no seu teclado')
                    break
                #jogar(matriz,linha,coluna,jogador)

#zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
                #zzzzzzzzzzzz   fase do jogador 2   zzzzzzzzzzzzzzzzzzzzzzzzz
            
                contador=1
                
                if contador==1:
                    jogador='0'
                    print('-------------JOGADOR 0-------------')
                    print("As casas onde tem 'X' ou '0' nao pode jogar")
                    
                    caso=verifica(matriz)
                    if caso==False:
                        debug=1
                        while debug==1:
                            
                            linhacoluna=int(input('Insira a posicao de acordo com o teclado: \n'))
                            if linhacoluna not in teclado:
                                debug=1
                            else:
                                debug=0
                        
                                print()
                        
                                if linhacoluna==7:
                                    linha=0
                                    coluna=0
                                    jogar(matriz,linha,coluna,jogador)

                                elif linhacoluna==8:
                                    linha=0
                                    coluna=1
                                    jogar(matriz,linha,coluna,jogador)

                                elif linhacoluna==9:
                                    linha=0
                                    coluna=2
                                    jogar(matriz,linha,coluna,jogador)

                                elif linhacoluna==4:
                                    linha=1
                                    coluna=0
                                    jogar(matriz,linha,coluna,jogador)
                
                                elif linhacoluna==5:
                                    linha=1
                                    coluna=1
                                    jogar(matriz,linha,coluna,jogador)
                
                                elif linhacoluna==6:
                                    linha=1
                                    coluna=2
                                    jogar(matriz,linha,coluna,jogador)

                                elif linhacoluna==1:
                                    linha=2
                                    coluna=0
                                    jogar(matriz,linha,coluna,jogador)

                                elif linhacoluna==2:
                                    linha=2
                                    coluna=1
                                    jogar(matriz,linha,coluna,jogador)

                                elif linhacoluna==3:
                                    linha=2
                                    coluna=2
                                    jogar(matriz,linha,coluna,jogador)

                                else:
                                    print('Vc precisa selecionar com base no eu teclado')
                                    break
                                print()
                        


                    else: #caso o resultado de CASO== TRUE, Entao temos um vencedor
                        print('Temos um vencedor')
                        caso=True
        

loop()



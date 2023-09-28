#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois
# informar quantas notas de cada valor serão fornecidas.
#As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
#O valor mínimo é de 10 reais e o máximo de 600 reais.
#O programa não deve se preocupar com a
#quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
#uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
#quatro notas de 10, uma nota de 5 e quatro notas de 1.
cem=0
cinquenta=0
dez=0
cinco=0
hum=0

print('BANCO DO BRASIL')

listUsuario=[]
listSenha=[]
listDeposito=[]
saque=0
dez=0
login=str(input('Insira seu nome de usuário: \n'))
listUsuario.append(login)
senha=str(input('Crie uma senha de usuário: \n '))
listSenha.append(senha)
deposito=float(input('Insira o valor do deposito: \n '))
listDeposito.append(deposito)


# area de login
print('-----------ÁREA DE LOGIN------------')
print('------------------------------------')

usuario=str(input('Insira o nome do Usuário: '))

if usuario in listUsuario:
    print('Insira sua senha ',usuario)
    password=(input('Insira sua senha:\n'))
    if password in listSenha:
    
        print('Login efetuado com sucesso!')
        print('--------------------------------')
        print()
        print('Vc deseja realizar algum saque? 1 para SIM ou 0 para NAO')
        confirma=int(input('Aguardando....: \n'))
        if confirma==1:
            print('Saldo disponivel: R$ ', listDeposito[0])
            print('Qual valor do saque o senhor deseja realizar: ')
            print('ATENÇÃO!! O valor minimo para este terminal eh de R$ 10 reais e no máximo R$ 600,00 reais')
            print('Para sacar outros valores, vc deve realizar outros saques.')
                 
            valor=int(input('Insira o valor do saque: R$ '))
            if valor>listDeposito[0]:
                print('Vc nao tem saldo disponivel')
            else:
                listDeposito.insert(0,(listDeposito[0]-valor))
                print('Saldo Disponível: R$ ',listDeposito[0])
                print()
                #valor eh igual a entrada
                if valor>=100:
                    cem=int(valor/100)
                    maior50=int(valor%100)


            #aki
                    if maior50>=50:
                        cinquenta=int(((valor%100))/50)
                        print('notas: ', cinquenta)
                        resto=int(valor%100)-50
                        
                        if resto>=10:
                            dez=int(resto/10)
                            #print('RESTO: ',resto)
                            if resto%10>=5:
                                
                                cinco=int((resto%10)/5)
                               
                                hum=int((resto%10)%5)

                                print('CINCO: ',cinco)
                                print('HUM: ',hum)
                            else:
                                hum=resto
                        else:
                            if resto>=5:
                                cinco=int(resto/5)
                                hum=int(resto%5)
                               
                            else:
                                
                                hum=resto
                                   # print('Restante: ',hum)
            #aki
                    else:                     
                                    

                        if maior50>=10:
                            dez=int(maior50/10)
                            if int(maior50%10)>=5:
                                resto=int((maior50%10))
                                cinco=int(resto/5)
                                hum=resto%5
                                
                            else:
                                hum=int(maior50%5)
                        
                         #   dez=int(maior50%10)
                         #   if dez>=5:
                         #       cinco=dez/5
                            #    hum=cinco%5

                           # else:
                          #      hum=dez
                        else:
                            if maior50>=5:
                                cinco=int(maior50/5)
                                hum=int(maior50%5)
                            else:
                                hum=maior50






     #                       unit=int(maior50/10)
      #                      if unit>5:
       #                         unidade=unit-5
        #                        resto=unidade/1
         #                       print(cem,maior50,unidade,resto)
          #                  else:unit/1
           #                 print('unit: ',unit)
            #            else:
             #               if maior50>5:
              #                  unit=maior50-5
               #                 resto=unit/1
                #                print('unidade:', unit)
                 #               print('resto: ',resto)
                  #          else:
                   #             unit=maior50/1
                    #            print('unidade: ',unit)
                #else:
                 #       if (valor%100)-50>5:
                  #          dez=int((valor%100)/10)
                   #         print('nota: ',dez)
                    #    else:
                     #       uniade=saque%100/5
                      #      resto=uniade%5
                       #     print('Unidade: ',uniade)
                        #    print('resto: ',resto)




                    

                print('Notas de 100: ',cem)
                print('Notas de 50: ',cinquenta)
                print('Notas de 10: ',dez)
                print('Notas de 5: ',cinco)
                print('Notas de 1: ',hum)
    else:
        print('Usuario ou senha inválido')

else:
    print('Usuario ou senha inválido')
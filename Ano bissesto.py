#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.


anobi=4

entrada=int(input('Insira o valor do ano: \n'))
if entrada%4==0:
    print('Esse ano eh bissesto')
else:
    print('Este ano nao eh bissesto')
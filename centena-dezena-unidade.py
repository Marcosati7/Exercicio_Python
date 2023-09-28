#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de:
#centenas, dezenas e unidades do mesmo
# imprima desta forma:
# 326 === 3 centenas     2 dezenas e 6 unidades
entrada=int(input('Insira um valor menor ou  igual a 1000: \n'))


if entrada>=100:

    centena=int(entrada/100)
    dezena=int((entrada%100)/10)
    unit=entrada%100
    unidade=unit%10

    print('Centenas: ', centena)
    print('Dezena: ',dezena)
    print('Unidade: ',unidade)
else:
    print('Dezena: ',int(entrada/10))
    print('Unidade: ',int(entrada%10))






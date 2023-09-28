# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.


data=[]
dma=['DIA','MES','ANO']


entrada=str(input('Insira a data no formato "DD/MM/AA: \n'))
data=entrada.split('/')


dataint=[]

for i in data:

    dataint.append(int(i))

# se vc digitou 12, n31=31
# se vc digitou 11, n30=30

mes30=[4,6,9,11]
mes31=[1,3,5,7,8,10,12]

print('data: ',data)

if dataint[1] in (mes30):
    print('mes de 30 dias')

    print('este mes recebe valores ate 30 dias')
    if dataint[0]>0 and dataint[0]<=30:
        print('Data informada corretamente')
    else: 
        print('Valor de dia incompativel')
if dataint[1] in (mes31):
    print('mes de 31 dias')
    print('Este mes recebe valor ate 31 dias')
    if dataint[0]>0 and dataint[0]<=31:
        print('Valor correto')
    else:
        print('valor dia nao corresponde ao mes de 31 dias')



lista=['1','2','3','4','5','5']

listaint=[]

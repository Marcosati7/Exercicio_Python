#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;
def configuracao(x,y,z):
    base1=x
    base2=y
    base3=z
    if base1==base2 and base1==base3:
       print('Isso eh um triangulo Equilatero')
       resultado="Equilátero"
    else:
        if base1==base2 or base1==base3 or base2==base3:
            print('Isso eh um triangulo Isosceles')
            resultado="Isosceles"
        else:
            print('Isso eh um triangulo escaleno')
            resultado="Escaleno"
    return(resultado)


x=0
triangulo=[]
for i in range(3):
    x=1
    print('Insira o ',x,' valor')
    entrada=int(input('Insira o valor: '))
    triangulo.append(entrada)
print(configuracao(triangulo[0],triangulo[1],triangulo[2]))

#equilatero = Todos os lados iguais
#isosceles = Dois lados iguais
# escaleno = Todos os lados difentes

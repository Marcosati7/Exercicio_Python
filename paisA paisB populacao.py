#Estrutura de Repetição
# atividade 4

#Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de 
#crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de crescimento de 1.5%.

#Faça um programa que calcule e escreva o número de anos necessários para que a população do país
#A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.




paisA=int(input('Insira a populaçao do pais A: '))
taxaA=float(input('Insira a taxa e cresciemento do pais A: '))

paisB=int(input('Insira a população do pais B: '))
taxaB=float(input('Insira a taxa de crescimento da população do pais B: '))

anos=0
while paisA<paisB:
    paisA=(paisA*taxaA+paisA)
    paisB=(paisB*taxaB+paisB)
    anos=anos+1

print('paisA ',int(paisA))
print('PaisB ', int(paisB))

print('Será necessario ', anos,' anos para o pais A igualar ao pais B')










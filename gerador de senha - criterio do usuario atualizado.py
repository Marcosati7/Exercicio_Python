# criar senha aleatoria com base nos critérios do usuario
import random
print('Senha com apenas numeros- selecione 1: ')
print('senha com apenas letras- selecione 2: ')
print('senha com numeros e letras - selecione 3: ')
print('senha com numeros e caracteres especiais - selecione 4: ')
print('senhas com numeros, letras e caracteres especiais - selecione 5: ')
print()
lista_lns=['a','c','b','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','&','*']
sorteio=[]
sorteio1=[]
# numero: 26 - 35   - #letras: 0-25 - #especiais: 36-42
def LetraNumero(sorteio,lista_lns,comeco1,fim1,comeco2,fim2):
    aleatorio=[]
    for i in range(1):
            for j in range(comeco1,fim1,1):
                aleatorio.append(lista_lns[j])
            sorteio.append(random.choice(aleatorio))
            #letras
    aleatorio=[]
    for i in range(1):
        #numeros
        for j in range(comeco2,fim2,1):
            aleatorio.append(lista_lns[j])
        sorteio.append(random.choice(aleatorio))
    return sorteio
#zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
            #começo do programa
entrada=int(input('Selecione a opcao desejada: '))
comprimento=int(input('Agora insira o comprimento da senha: '))
if entrada>0 or comprimento>0:
    if entrada==1:
        for i in range(comprimento):
            for j in range(26,35,1):
                aleatorio=lista_lns[j]
                sorteio1.append(aleatorio)
            sorteio.append(random.choice(sorteio1))
        print('Sorteio: ',sorteio)
#zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
    elif entrada==2:
        for i in range(comprimento):
            for j in range(0,25,1):
                aleatorio=lista_lns[j]
                sorteio1.append(aleatorio)
            sorteio.append(random.choice(sorteio1))
        print('Sorteio: ',sorteio)
#zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
    elif entrada==3:
        comeco1=0;        fim1=25;        comeco2=26;        fim2=35
        LetraNumero(sorteio,lista_lns,comeco1,fim1,comeco2,fim2)
        print('Valor de sorteio eh: ',sorteio)
        for i in range(comprimento-2):
            for j in range(0,35,1):
                aleatorio=lista_lns[j]
                sorteio1.append(aleatorio)
            sorteio.append(random.choice(sorteio1))
        print('Sorteio: ',sorteio)
    elif entrada==4:
        comeco1=26;  fim1=35;        comeco2=36;        fim2=42
        LetraNumero(sorteio,lista_lns,comeco1,fim1,comeco2,fim2)
        print('Valor de sorteio eh: ',sorteio)
        for i in range(comprimento-2):
            for j in range(26,42,1):
                aleatorio=lista_lns[j]
                sorteio1.append(aleatorio)
            sorteio.append(random.choice(sorteio1))
        print('Sorteio: ',sorteio)
    elif entrada==5:
        comeco1=0; fim1=42;comeco2=0;fim2=42
        LetraNumero(sorteio,lista_lns,comeco1,fim1,comeco2,fim2)
        print('Valor de sorteio eh: ',sorteio)
        for i in range(comprimento-3):
            for j in range(0,42,1):
                aleatorio=lista_lns[j]
                sorteio1.append(aleatorio)
            sorteio.append(random.choice(sorteio1))
        print('Sorteio: ',sorteio)
else:
    print('Vc nao pode selecionar zero nem para entrada, muito menos para comprimento')
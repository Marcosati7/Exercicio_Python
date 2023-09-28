import hashlib
import mysql.connector


def verificar_login(user,senha):
    cpf=user
    senha=senha

    hash=hashlib.sha256(senha.encode('utf-8'))
    senha=hash.hexdigest()

    bd_connection=mysql.connector.connect(host='localhost',user='root',password='',database='bancocentral')
    cursor=bd_connection.cursor()
    cursor.execute('select cpf,senha from cadastro where cpf=%s and senha=%s',(cpf,senha))
    resposta=cursor.fetchall()
    if resposta:
        print('correto')
        verifica=True
    else:
        print('incorreto')
        verifica=False


    return verifica
    


# nome - cpf - email - endereco - senha


# insira seu nome
# insira sua senha 
#( verificar no banco de dados se existe este usuario) - chamar funcao verifica
#realizar um hashe sha256 e entao verificar se o msmo tem no banco de dados usando a funcao
# usuario ou senha inválida

laco=True

while laco==True:
    user=str(input('Insira seu CPF: \n'))
    senha=str(input('insira sua senha: \n'))

    if verificar_login(user,senha):
        laco=False
    else:
        print('Usuário ou senha incorreto')
        print('Vc deseja tentar novamente ou realize um cadastro conosco? Selecione 1 para SIM ou 2 para cadastrar\n')
        entrada=int(input('Selecione 1 ou 2: \n'))
        if entrada==1:
            laco=True
        else:
            # criar uma funcao para realizar cadastro
            pass

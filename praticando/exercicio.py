#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

def verificador_de_numeros():
    numero = int(input('Digite um numero: '))
    
    if numero % 2 == 0:
        print('Esse nuemro é PAR')
    else:
        print('Esse nuemro é IMPAR')
#verificador_de_numeros()

#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.

def verificador_de_idade():
    idade = int(input('Digite sua idade :'))

    if   0 <= idade <= 12:
        print('Voce ainda é criança')
    elif 13 <= idade <= 17:
        print('Voce ainda é adolescente')
    elif idade > 18:
        print('Voce ainda é adulto')
    else:
        print('Erro')
#verificador_de_idade()

#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

def login():
    usuario_teste  = 'ADS'
    senha_teste = 1234
    
    usuario = input('Digite seu nome de usuario:')
    senha = int(input('Digite sua senha:'))
    
    if usuario == usuario_teste and senha == senha_teste:
        print('Login concluido com sucesso')
    else:
        print('ERRO, senha ou usuario incorreto')

#login()

#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.

def plano_cartesiano():
    
    x = int(input('Digite a cordenadas de X: '))
    y = int(input('Digite a cordenadas de Y: '))

    if x > 0 and y > 0:
        print(f'A as cordenadas [{x}] e [{y}] são do primeiro quadrante')
    elif x < 0 and y > 0:
        print(f'A as cordenadas [{x}] e [{y}] são do segundo quadrante')
    elif x < 0  and y < 0:
        print(f'A as cordenadas [{x}] e [{y}] são do terceiro quadrante')
    elif x > 0 and y < 0: 
        print(f'A as cordenadas [{x}] e [{y}] são do quarto quadrante')
    else:
        print('O ponto está localizado no eixo ou origem.')

#plano_cartesiano()


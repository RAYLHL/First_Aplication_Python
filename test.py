
def calculo_basico():

    operacoes = {'soma','subtração','divisão','multiplicação'}
    print(operacoes)

    operacao = input('Qual tipo de operação tu quer fazer: ').strip().lower()
    x = int(input('Digite o primeiro numero seu burro : '))
    y = int(input('Digite o segundo  numero seu burro : '))

    if operacao == 'soma':
        print(x + y )
    elif operacao == 'subtração':
        print(x - y )
    elif operacao == 'divisão':
        print(int(x / y ))
    elif operacao == 'multiplicação':
        print(x * y )
    else:
        print("erro")

calculo_basico()

    
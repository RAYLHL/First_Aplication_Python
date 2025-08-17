#1 - Crie uma lista para cada informação a seguir:

#Lista de números de 1 a 10;
#Lista com quatro nomes;
#Lista com o ano que você nasceu e o ano atual.
 
lista = [1,2,3,4,5,6,7,8,9,10]  #existem 2 tipos  jeito "mais burro"
print(lista)

numeros = list(range(1, 11))  #jeito mais inteligente 
print(numeros)

lista_nomes = ["GYM","chest","legs","back"]
print(lista_nomes)

anos = [2003, 2025]  # exemplo: nasceu em 2003 e o ano atual é 2025
print(anos)

#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

numeros = list(range(1, 11))  # jeito mais inteligente
print(numeros)

for numero in numeros:
    print(numero)

#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.


numeros = list(range(1, 20))  # jeito mais inteligente
print(numeros)

soma = 0  # acumulador para somar os ímpares

for numero in numeros:
    if numero % 2 != 0:
        soma += numero


print(f"A soma dos números ímpares de 1 a 20 é: {soma}")

#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

for numero in range(10, 0, -1):  # começa em 10, vai até 1, decrementa 1
    print(numero)

#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

def tabuada():
    multiplicadores = list(range(1, 11))

    numero = int(input('Qual numero gostaria de imprimir a tabuada: '))
    print(f'A tabuado do {numero} é:')

    for multiplicador in multiplicadores:
        resultado = numero * multiplicador
        print(f'{numero} x {multiplicador} = {resultado}')      
#tabuada()        


#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

lista_numeros = list(range(1, 11))  # cria lista de 1 a 10
soma = 0  # acumulador

try:
    for numero in lista_numeros:
        soma += numero  # soma os elementos
    print(f"A soma dos números da lista é: {soma}")

except Exception as erro:
    print(f"Ocorreu um erro: {erro}")

#7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.


lista_numeros = [10, 20, 30, 40, 50]  # exemplo de lista

try:
    media = sum(lista_numeros) / len(lista_numeros)
    print(f"A média dos valores é: {media:.2f}")

except ZeroDivisionError:
    print("Erro: não é possível calcular a média de uma lista vazia.")
#1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

informacoes = [{'nome':'Rayl', 'idade':18, 'cidade': 'Navegantes'},
               {'nome':'henrique', 'idade':23, 'cidade': 'itajai'}
               ] # isso é uma lista de dicionarios / Observação: é melhor usar números para idades, não strings, caso queira fazer operações matemáticas depois.

informacoes2 = {    
    'nome': 'Rayl',
    'idade': 18,
    'cidade': 'Navegantes'
    }  #unico dicionario
print(informacoes2)  

#2 - Utilizando o dicionário criado no item 1:

#Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
informacoes = {
    'nome': 'Rayl',
    'idade': 18,
    'cidade': 'Navegantes'
}

# Atualizando a idade
informacoes['idade'] = 19  

print(informacoes)
#Adicione um campo de profissão para essa pessoa;
informacoes['profissao'] = 'vagabundo'

print(informacoes)
#Remova um item do dicionário.
informacoes = {
    'nome': 'Rayl',
    'idade': 18,
    'cidade': 'Navegantes',
    'profissao': 'vagabundo'
}

del informacoes['profissao']
# ou usando pop:
# informacoes.pop('profissao')
print(informacoes)


#3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
quadrados = {
    1: 1**2,
    2: 2**2,
    3: 3**2,
    4: 4**2,
    5: 5**2    
}

quadrados = {x: x**2 for x in range(1, 20)}
print(quadrados)
#4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
dados = {
    'casa': 'azul',
    'carro': 'preto',
    'bicicleta':'cinza'
}
chave = 'casa'

if chave in dados:
    print(f"A chave '{chave}' existe no dicionário!")
else:
    print(f"A chave '{chave}' não existe no dicionário.")
    

#5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
frase = "o cachorro correu atrás do outro cachorro"
frase = frase.lower()  # opcional: deixa todas as palavras minúsculas
palavras = frase.split()  # separa a frase em palavras

frequencia = {}

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print(frequencia)
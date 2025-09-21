
#Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo 
        self.cor = cor 
        self.ano = ano 
    
    def __str__(self):
        return f"Carro (modelo = {self.modelo} | cor = {self.cor} | ano = {self.ano})"
    
carro_antigo = Carro('mustang', 'azul' , 1990)
carro_novo = Carro('Corola', 'preto', 2020)

print(carro_antigo)
print(carro_novo)

#Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
class Restaurante:
    def __init__(self, nome, categoria, ativo, localizacao, delivery):
        self.nome = nome
        self.categoria = categoria 
        self.ativo = False  
        self.localizacao = localizacao
        self.delivery = False 

    def __str__(self):
        status = "Ativo" if self.ativo else "Inativo"
        entrega = "faz delivery" if self.delivery else "não faz delivery"
        return (f'O restaurante {self.nome} | de categoria {self.categoria} | esta localizado na {self.localizacao} | Status: {status} | Entrega: {entrega}' )

#restaurante_italiana = Restaurante('Italiana Garden', 'Restaurante','Rua 123')
restaurante_italiana = Restaurante(
    nome='Italiana Garden',
    categoria='Italiana',
    ativo=False,
    localizacao='Rua 123',
    delivery=True
)
print(restaurante_italiana)


#Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome 
        self.categoria = categoria
        self.ativo = False
        self.localizacao = None
        self.delivery = False

    def __str__(self):
        status = 'Ativo' if self.ativo else 'Inativo'
        entrega = 'Faz delivery' if self.delivery else 'não faz delivery '
        return (f'O resturante {self.nome} | Categoria: {self.categoria}'
                f'Status: {status} | Entrega: {entrega}')        
    
restaurante_italiana = Restaurante('Sabor da Italia', 'Italiana')

print(restaurante_italiana)

#Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.


#ja foi feito ali emcima

#Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:
    def __init__(self,nome , genero, idade, cliente):
        self.nome = nome 
        self.genero = genero 
        self.idade = idade 
        self.cliente = cliente

    def __str__(self):
        status = 'Cliente' if self.cliente else 'Não é cliente'
        return f'{self.nome} | {self.genero} | {self.idade} | {status}'

loja_dez = Cliente('João','Masculino', 20, True)
loja_mio = Cliente('Maria','Femenino ', 19, True)
loja_comper = Cliente('Gaybriel','Masculino', 23, False)


print(loja_comper)


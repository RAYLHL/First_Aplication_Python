from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome , categoria): 
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self.nome} | {self.categoria}' 
    
    @classmethod
    def listar_restaurante(cls):
        print(f'{'Nome do resrtaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes: 
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}' )

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'false'
    
    def alterar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)


    

restaurante_ifood = Restaurante('ifood','Comida de aplicativo') 
restaurante_ifood.alterar_estado()
restaurante_KILO = Restaurante('KILO','Comida de Restaurante')

Restaurante.listar_restaurante()
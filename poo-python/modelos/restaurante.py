from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome , categoria): 
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self.nome} | {self.categoria}' 
    
    @classmethod
    def listar_restaurante(cls):
        print(f'{'Nome do resrtaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliacao'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes: 
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}' )

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'false'
    
    def alterar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
 
    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-' 
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return  media
    

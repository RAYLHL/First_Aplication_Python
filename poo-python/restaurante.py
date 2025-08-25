class Restaurante:
    def __init__(self, nome , categoria): 
        self.nome = nome 
        self.categoria = categoria
        self.ativo = False
    def __str__(self):
        return f'{self.nome} | {self.categoria}' 

restaurante_ifood = Restaurante('ifood','Comida de aplicativo') 
restaurante_KILO = Restaurante('KILO','Comida de Restaurante')

restaurantes = [restaurante_ifood, restaurante_KILO]

print(restaurante_ifood)
print(restaurante_KILO)
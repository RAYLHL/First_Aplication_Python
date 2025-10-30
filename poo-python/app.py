from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_japones = Restaurante('Japa',' Comida Japonesa ')
bebida_suco = Bebida('Suco de Laranja', 8.00, '300ml')
prato_shushi = Prato('Sushi', 25.00, 'Sushi de Salmão com arroz e alga')

def main():
    print(bebida_suco)
    print(prato_shushi)

if __name__ == '__main__':
    main()
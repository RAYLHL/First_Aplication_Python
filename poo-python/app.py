from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_japones = Restaurante('Japa',' Comida Japonesa ')
bebida_suco = Bebida('Suco de Laranja', 8.00, '300ml')
prato_shushi = Prato('Sushi', 25.00, 'Sushi de Salmão com arroz e alga')
prato_macarrao = Prato('Macarrão',10.00, 'Macarrão ao molho')
restaurante_japones.adicionar_no_cardapio(bebida_suco)
restaurante_japones.adicionar_no_cardapio(prato_shushi)


def main():
   restaurante_japones.exibir_cardapio

if __name__ == '__main__':
    main()
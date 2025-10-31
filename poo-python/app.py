from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.sobremesa import Sobremesa

restaurante_japones = Restaurante('Japa',' Comida Japonesa ')
bebida_suco = Bebida('Suco de Laranja', 8.00, '300ml')
bebida_suco.aplicar_desconto()
prato_shushi = Prato('Sushi', 25.00, 'Sushi de Salmão com arroz e alga')
prato_shushi.aplicar_desconto()
prato_macarrao = Prato('Macarrão',10.00, 'Macarrão ao molho')
sobremesa_cookie = Sobremesa('Cookie', 5.00, 'Sobremesa Biscoito', 'medio', 'Cookie de chocolate')
restaurante_japones.adicionar_no_cardapio(sobremesa_cookie)
restaurante_japones.adicionar_no_cardapio(bebida_suco)
restaurante_japones.adicionar_no_cardapio(prato_shushi)


def main():
   restaurante_japones.exibir_cardapio

if __name__ == '__main__':
    main()
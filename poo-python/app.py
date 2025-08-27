from modelos.restaurante import Restaurante

restaurante_japones = Restaurante('Japa',' Comida Japonesa ')
restaurante_japones.receber_avaliacao('Rayl', 9)

def main():
    Restaurante.listar_restaurante()

if __name__ == '__main__':
    main()
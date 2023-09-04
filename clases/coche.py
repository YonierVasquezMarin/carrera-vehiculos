from clases.vehiculo import Vehiculo
from decoradores.turbo import turbo


class Coche(Vehiculo):
    def __init__(self, velocidadMaxima, capacidadCombustible):
        super().__init__(velocidadMaxima, capacidadCombustible)

    @turbo
    def acelerar(self, distancia):
        super().acelerar(distancia+10)

    def frenar(self, distancia):
        super().frenar(distancia-5)




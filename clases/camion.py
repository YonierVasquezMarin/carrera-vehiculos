from clases.vehiculo import Vehiculo


class Camion(Vehiculo):
    def __init__(self, velocidadMaxima, capacidadCombustible):
        super().__init__(velocidadMaxima, capacidadCombustible)

    def acelerar(self, distancia):
        super().acelerar(distancia+5)

    def frenar(self, distancia):
        super().frenar(distancia-5)
